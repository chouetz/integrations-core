# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from types import MappingProxyType
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class AuthToken(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    reader: Optional[MappingProxyType[str, Any]] = None
    writer: Optional[MappingProxyType[str, Any]] = None


class IncludeItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    name: Optional[str] = None
    uptime: Optional[bool] = None


class Node(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, IncludeItem], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of nodes to be processed.\n')
    portgroups: Optional[Union[bool, MappingProxyType[str, Any]]] = None


class Volume(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    connectors: Optional[bool] = None
    targets: Optional[bool] = None


class BaremetalItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    allocations: Optional[bool] = None
    conductors: Optional[bool] = None
    drivers: Optional[bool] = None
    nodes: Optional[Union[bool, Node]] = None
    ports: Optional[bool] = None
    volumes: Optional[Union[bool, Volume]] = None


class BlockStorageItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    clusters: Optional[bool] = None
    pools: Optional[bool] = None
    snapshots: Optional[bool] = None
    transfers: Optional[bool] = None
    volumes: Optional[bool] = None


class Hypervisor(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, IncludeItem], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of hypervisors to be processed.\n')


class IncludeItem2(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    diagnostics: Optional[bool] = None
    flavors: Optional[bool] = None
    name: Optional[str] = None


class Server(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, IncludeItem2], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of servers to be processed.\n')


class ComputeItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    flavors: Optional[bool] = None
    hypervisors: Optional[Union[bool, Hypervisor]] = None
    limits: Optional[bool] = None
    quota_sets: Optional[bool] = None
    servers: Optional[Union[bool, Server]] = None
    services: Optional[bool] = None


class HeatItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    stacks: Optional[bool] = None


class IdentityItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    domains: Optional[bool] = None
    groups: Optional[bool] = None
    limits: Optional[bool] = None
    projects: Optional[bool] = None
    regions: Optional[bool] = None
    services: Optional[bool] = None
    users: Optional[bool] = None


class Image(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    members: Optional[bool] = None


class ImageItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    images: Optional[Union[bool, Image]] = None


class IncludeItem3(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    id: Optional[str] = None
    stats: Optional[bool] = None


class AmphoraeItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, IncludeItem3], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of amphorae to be processed.\n')


class IncludeItem4(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    name: Optional[str] = None


class Healthmonitor(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, IncludeItem4], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of healthmonitors to be processed.\n')


class IncludeItem5(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    name: Optional[str] = None
    stats: Optional[bool] = None


class Listener(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, IncludeItem5], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of listeners to be processed.\n')


class Loadbalancer(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, IncludeItem5], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of loadbalancers to be processed.\n')


class IncludeItem8(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    name: Optional[str] = None


class Member(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, IncludeItem8], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of members to be processed.\n')


class IncludeItem7(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    members: Optional[Union[bool, Member]] = None
    name: Optional[str] = None


class Pool(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    include: Optional[tuple[Union[str, IncludeItem7], ...]] = None
    limit: Optional[int] = Field(None, description='Maximum number of pools to be processed.\n')


class IncludeItem9(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    name: Optional[str] = None


class Quota(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, IncludeItem9], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of quotas to be processed.\n')


class LoadBalancerItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    amphorae: Optional[Union[bool, AmphoraeItem]] = None
    healthmonitors: Optional[Union[bool, Healthmonitor]] = None
    listeners: Optional[Union[bool, Listener]] = None
    loadbalancers: Optional[Union[bool, Loadbalancer]] = None
    pools: Optional[Union[bool, Pool]] = None
    quotas: Optional[Union[bool, Quota]] = None


class Network(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, IncludeItem9], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of networks to be processed.\n')


class NetworkItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    agents: Optional[bool] = None
    networks: Optional[Union[bool, Network]] = None
    quotas: Optional[bool] = None


class SwiftItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    containers: Optional[bool] = None


class Components(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    baremetal: Optional[Union[bool, BaremetalItem]] = None
    block_storage: Optional[Union[bool, BlockStorageItem]] = Field(None, alias='block-storage')
    compute: Optional[Union[bool, ComputeItem]] = None
    heat: Optional[Union[bool, HeatItem]] = None
    identity: Optional[Union[bool, IdentityItem]] = None
    image: Optional[Union[bool, ImageItem]] = None
    load_balancer: Optional[Union[bool, LoadBalancerItem]] = Field(None, alias='load-balancer')
    network: Optional[Union[bool, NetworkItem]] = None
    swift: Optional[Union[bool, SwiftItem]] = None


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[str, ...]] = None


class Projects(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, MappingProxyType[str, Any]], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of clusters to be processed.\n')


class Proxy(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    http: Optional[str] = None
    https: Optional[str] = None
    no_proxy: Optional[tuple[str, ...]] = None


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        arbitrary_types_allowed=True,
        frozen=True,
    )
    allow_redirects: Optional[bool] = None
    auth_token: Optional[AuthToken] = None
    auth_type: Optional[str] = None
    aws_host: Optional[str] = None
    aws_region: Optional[str] = None
    aws_service: Optional[str] = None
    blacklist_project_names: Optional[tuple[str, ...]] = None
    cinder_microversion: Optional[str] = None
    collect_hypervisor_load: Optional[bool] = None
    collect_hypervisor_metrics: Optional[bool] = None
    collect_network_metrics: Optional[bool] = None
    collect_project_metrics: Optional[bool] = None
    collect_server_diagnostic_metrics: Optional[bool] = None
    collect_server_flavor_metrics: Optional[bool] = None
    components: Optional[Components] = None
    connect_timeout: Optional[float] = None
    disable_generic_tags: Optional[bool] = None
    domain_id: Optional[str] = None
    empty_default_hostname: Optional[bool] = None
    endpoint_interface: Optional[str] = None
    endpoint_region_id: Optional[str] = None
    exclude_network_ids: Optional[tuple[str, ...]] = None
    exclude_server_ids: Optional[tuple[str, ...]] = None
    extra_headers: Optional[MappingProxyType[str, Any]] = None
    headers: Optional[MappingProxyType[str, Any]] = None
    ironic_microversion: Optional[str] = None
    kerberos_auth: Optional[str] = None
    kerberos_cache: Optional[str] = None
    kerberos_delegate: Optional[bool] = None
    kerberos_force_initiate: Optional[bool] = None
    kerberos_hostname: Optional[str] = None
    kerberos_keytab: Optional[str] = None
    kerberos_principal: Optional[str] = None
    keystone_server_url: Optional[str] = None
    log_requests: Optional[bool] = None
    metric_patterns: Optional[MetricPatterns] = None
    min_collection_interval: Optional[float] = None
    name: Optional[str] = None
    nova_microversion: Optional[str] = None
    ntlm_domain: Optional[str] = None
    openstack_cloud_name: Optional[str] = None
    openstack_config_file_path: Optional[str] = None
    paginated_limit: Optional[int] = None
    password: Optional[str] = None
    persist_connections: Optional[bool] = None
    projects: Optional[Projects] = None
    proxy: Optional[Proxy] = None
    read_timeout: Optional[float] = None
    request_size: Optional[float] = None
    service: Optional[str] = None
    skip_proxy: Optional[bool] = None
    tags: Optional[tuple[str, ...]] = None
    timeout: Optional[float] = None
    tls_ca_cert: Optional[str] = None
    tls_cert: Optional[str] = None
    tls_ignore_warning: Optional[bool] = None
    tls_private_key: Optional[str] = None
    tls_protocols_allowed: Optional[tuple[str, ...]] = None
    tls_use_host_header: Optional[bool] = None
    tls_verify: Optional[bool] = None
    use_agent_proxy: Optional[bool] = None
    use_legacy_auth_encoding: Optional[bool] = None
    use_legacy_check_version: Optional[bool] = None
    use_shortname: Optional[bool] = None
    user: Optional[MappingProxyType[str, Any]] = None
    username: Optional[str] = None
    whitelist_project_names: Optional[tuple[str, ...]] = None

    @model_validator(mode='before')
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @field_validator('*', mode='before')
    def _validate(cls, value, info):
        field = cls.model_fields[info.field_name]
        field_name = field.alias or info.field_name
        if field_name in info.context['configured_fields']:
            value = getattr(validators, f'instance_{info.field_name}', identity)(value, field=field)
        else:
            value = getattr(defaults, f'instance_{info.field_name}', lambda: value)()

        return validation.utils.make_immutable(value)

    @model_validator(mode='after')
    def _final_validation(cls, model):
        return validation.core.check_model(getattr(validators, 'check_instance', identity)(model))
