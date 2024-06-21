# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import pytest

from datadog_checks.base.constants import ServiceCheck
from datadog_checks.dev.utils import get_metadata_metrics
from datadog_checks.kubernetes_cluster_autoscaler import KubernetesClusterAutoscalerCheck

from .common import METRICS_MOCK, get_fixture_path


def test_check_kubernetes_cluster_autoscaler(dd_run_check, aggregator, instance, mock_http_response):
    mock_http_response(file_path=get_fixture_path('kubernetes_cluster_autoscaler_metrics.txt'))
    check = KubernetesClusterAutoscalerCheck('kubernetes_cluster_autoscaler', {}, [instance])
    dd_run_check(check)

    for metric in METRICS_MOCK:
        aggregator.assert_metric(metric)
        aggregator.assert_metric_has_tag(metric, 'test:test')

    aggregator.assert_all_metrics_covered()
    aggregator.assert_metrics_using_metadata(get_metadata_metrics())
    aggregator.assert_service_check('kubernetes_cluster_autoscaler.openmetrics.health', ServiceCheck.OK)


def test_empty_instance(dd_run_check):
    with pytest.raises(
        Exception,
        match='InstanceConfig`:\nopenmetrics_endpoint\n  Field required',
    ):
        check = KubernetesClusterAutoscalerCheck('KubernetesClusterAutoscalerCheck', {}, [{}])
        dd_run_check(check)
