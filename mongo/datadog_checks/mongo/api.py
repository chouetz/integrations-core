# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from pymongo import MongoClient, ReadPreference
from pymongo.errors import (
    ConfigurationError,
    ConnectionFailure,
    OperationFailure,
    ProtocolError,
    ServerSelectionTimeoutError,
)

from datadog_checks.mongo.common import (
    MongosDeployment,
    ReplicaSetDeployment,
    StandaloneDeployment,
)

# The name of the application that created this MongoClient instance. MongoDB 3.4 and newer will print this value in
# the server log upon establishing each connection. It is also recorded in the slow query log and profile collections.
DD_APP_NAME = 'datadog-agent'

# We collect here all pymongo exceptions that would result in a CRITICAL service check.
CRITICAL_FAILURE = (
    ConfigurationError,  # This occurs when TLS is misconfigured.
    ConnectionFailure,  # This is a generic exception for any problems when connecting to mongodb.
    OperationFailure,  # This occurs when authentication is incorrect.
    # This means either no server is available or a replicaset has not elected a primary in the timeout window.
    # In both cases it makes sense to submit a CRITICAL service check to Datadog.
    ServerSelectionTimeoutError,
    # Errors at the level of the protocol result in a lost/degraded connection. We can issue a CRITICAL check for this.
    ProtocolError,
)


class MongoApi(object):
    """Mongodb connection through pymongo.MongoClient

    :params config: MongoConfig object.
    :params log: Check log.
    :params replicaset: If replication is enabled, this parameter specifies the name of the replicaset.
        Valid for ReplicaSetDeployment deployments
    """

    def __init__(self, config, log, replicaset: str = None):
        self._config = config
        self._log = log
        options = {
            'host': self._config.server if self._config.server else self._config.hosts,
            'socketTimeoutMS': self._config.timeout,
            'connectTimeoutMS': self._config.timeout,
            'serverSelectionTimeoutMS': self._config.timeout,
            'directConnection': True,
            'read_preference': ReadPreference.PRIMARY_PREFERRED,
            'appname': DD_APP_NAME,
        }
        if replicaset:
            options['replicaSet'] = replicaset
        options.update(self._config.additional_options)
        options.update(self._config.tls_params)
        if self._config.do_auth and not self._is_arbiter(options):
            self._log.info("Using '%s' as the authentication database", self._config.auth_source)
            if self._config.username:
                options['username'] = self._config.username
            if self._config.password:
                options['password'] = self._config.password
            if self._config.auth_source:
                options['authSource'] = self._config.auth_source
        self._log.debug("options: %s", options)
        self._cli = MongoClient(**options)
        self.deployment_type = None

    def __getitem__(self, item):
        return self._cli[item]

    def connect(self):
        try:
            # The ping command is cheap and does not require auth.
            self['admin'].command('ping')
        except ConnectionFailure as e:
            self._log.debug('ConnectionFailure: %s', e)
            raise

    def server_info(self, session=None):
        return self._cli.server_info(session)

    def list_database_names(self, session=None):
        return self._cli.list_database_names(session)

    def current_op(self, session=None):
        # Use $currentOp stage to get all users and idle sessions.
        # Note: Why not use the `currentOp` command?
        # Because the currentOp command and db.currentOp() helper method return the results in a single document,
        # the total size of the currentOp result set is subject to the maximum 16MB BSON size limit for documents.
        # The $currentOp stage returns a cursor over a stream of documents, each of which reports a single operation.
        return self["admin"].aggregate([{'$currentOp': {'allUsers': True}}], session=session)

    def _is_arbiter(self, options):
        cli = MongoClient(**options)
        is_master_payload = cli['admin'].command('isMaster')
        return is_master_payload.get('arbiterOnly', False)

    def _get_rs_deployment_from_status_payload(self, repl_set_payload, is_master_payload, cluster_role):
        replset_name = repl_set_payload["set"]
        replset_state = repl_set_payload["myState"]
        hosts = [m['name'] for m in repl_set_payload.get("members", [])]
        replset_me = is_master_payload.get('me')
        return ReplicaSetDeployment(replset_name, replset_state, hosts, replset_me, cluster_role=cluster_role)

    def refresh_deployment_type(self):
        # getCmdLineOpts is the runtime configuration of the mongo instance. Helpful to know whether the node is
        # a mongos or mongod, if the mongod is in a shard, if it's in a replica set, etc.
        try:
            self.deployment_type = self._get_default_deployment_type()
        except Exception as e:
            self._log.debug(
                "Unable to run `getCmdLineOpts`, got: %s. Treating this as an Alibaba ApsaraDB instance.", str(e)
            )
            try:
                self.deployment_type = self._get_alibaba_deployment_type()
            except Exception as e:
                self._log.debug("Unable to run `shardingState`, so switching to AWS DocumentDB, got error %s", str(e))
                self.deployment_type = self._get_documentdb_deployment_type()

    def _get_default_deployment_type(self):
        options = self['admin'].command("getCmdLineOpts")['parsed']
        cluster_role = None
        if 'sharding' in options:
            if 'configDB' in options['sharding']:
                self._log.debug("Detected MongosDeployment. Node is principal.")
                return MongosDeployment(shard_map=self.refresh_shards())
            elif 'clusterRole' in options['sharding']:
                cluster_role = options['sharding']['clusterRole']

        replication_options = options.get('replication', {})
        if 'replSetName' in replication_options or 'replSet' in replication_options:
            repl_set_payload = self['admin'].command("replSetGetStatus")
            is_master_payload = self['admin'].command('isMaster')
            replica_set_deployment = self._get_rs_deployment_from_status_payload(
                repl_set_payload, is_master_payload, cluster_role
            )
            is_principal = replica_set_deployment.is_principal()
            is_principal_log = "" if is_principal else "not "
            self._log.debug("Detected ReplicaSetDeployment. Node is %sprincipal.", is_principal_log)
            return replica_set_deployment

        self._log.debug("Detected StandaloneDeployment. Node is principal.")
        return StandaloneDeployment()

    def _get_alibaba_deployment_type(self):
        is_master_payload = self['admin'].command('isMaster')
        if is_master_payload.get('msg') == 'isdbgrid':
            return MongosDeployment(shard_map=self.refresh_shards())

        # On alibaba cloud, a mongo node is either a mongos or part of a replica set.
        repl_set_payload = self['admin'].command("replSetGetStatus")
        if repl_set_payload.get('configsvr') is True:
            cluster_role = 'configsvr'
        elif self['admin'].command('shardingState').get('enabled') is True:
            # Use `shardingState` command to know whether or not the replicaset
            # is a shard or not.
            cluster_role = 'shardsvr'
        else:
            cluster_role = None
        return self._get_rs_deployment_from_status_payload(repl_set_payload, is_master_payload, cluster_role)

    def _get_documentdb_deployment_type(self):
        """
        Deployment type for AWS DocumentDB.

        We connect to "Instance Based Clusters". In MongoDB terms, these are unsharded replicasets.
        """
        repl_set_payload = self['admin'].command("replSetGetStatus")
        is_master_payload = self['admin'].command('isMaster')
        return self._get_rs_deployment_from_status_payload(repl_set_payload, is_master_payload, cluster_role=None)

    def refresh_shards(self):
        try:
            shard_map = self['admin'].command('getShardMap')
            self._log.debug('Get shard map: %s', shard_map)
            return shard_map
        except Exception as e:
            self._log.error('Unable to get shard map for mongos: %s', e)
            return {}

    def server_status(self):
        return self['admin'].command('serverStatus')

    @property
    def hostname(self):
        try:
            hostname = self.server_status()['host'].split(':')
            if len(hostname) == 1:
                # If there is no port, we assume the default port
                return "{}:27017".format(hostname[0])
            else:
                return "{}:{}".format(hostname[0], hostname[1])
        except Exception as e:
            self._log.error('Unable to get hostname: %s', e)
            return None
