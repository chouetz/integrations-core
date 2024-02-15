# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

import pytest

from datadog_checks.dev import docker_run
from datadog_checks.dev.conditions import WaitForPortListening
from datadog_checks.dev.fs import get_here

VCSIM_INSTANCE = {'esxi_url': '127.0.0.1', 'port': 8989, 'username': 'test', 'password': 'test'}

BASE_INSTANCE = {'esxi_url': 'localhost', 'username': 'test', 'password': 'test'}


@pytest.fixture(scope='session')
def dd_environment():
    compose_file = os.path.join(get_here(), 'docker', 'docker-compose.yaml')
    conditions = [WaitForPortListening('127.0.0.1', 8989, wait=4)]
    with docker_run(compose_file, conditions=conditions):

        yield VCSIM_INSTANCE


@pytest.fixture
def instance():
    return BASE_INSTANCE


@pytest.fixture
def vcsim_instance():
    return VCSIM_INSTANCE
