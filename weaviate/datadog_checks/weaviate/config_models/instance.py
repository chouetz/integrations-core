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


class ExtraMetrics(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra='allow',
        frozen=True,
    )
    name: Optional[str] = None
    type: Optional[str] = None


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[str, ...]] = None


class Metrics(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra='allow',
        frozen=True,
    )
    name: Optional[str] = None
    type: Optional[str] = None


class Proxy(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    http: Optional[str] = None
    https: Optional[str] = None
    no_proxy: Optional[tuple[str, ...]] = None


class ShareLabels(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    labels: Optional[tuple[str, ...]] = None
    match: Optional[tuple[str, ...]] = None


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
    cache_metric_wildcards: Optional[bool] = None
    cache_shared_labels: Optional[bool] = None
    collect_counters_with_distributions: Optional[bool] = None
    collect_histogram_buckets: Optional[bool] = None
    connect_timeout: Optional[float] = None
    disable_generic_tags: Optional[bool] = None
    empty_default_hostname: Optional[bool] = None
    enable_health_service_check: Optional[bool] = None
    exclude_labels: Optional[tuple[str, ...]] = None
    exclude_metrics: Optional[tuple[str, ...]] = None
    exclude_metrics_by_labels: Optional[MappingProxyType[str, Union[bool, tuple[str, ...]]]] = None
    extra_headers: Optional[MappingProxyType[str, Any]] = None
    extra_metrics: Optional[tuple[Union[str, MappingProxyType[str, Union[str, ExtraMetrics]]], ...]] = None
    headers: Optional[MappingProxyType[str, Any]] = None
    histogram_buckets_as_distributions: Optional[bool] = None
    hostname_format: Optional[str] = None
    hostname_label: Optional[str] = None
    ignore_connection_errors: Optional[bool] = None
    ignore_tags: Optional[tuple[str, ...]] = None
    include_labels: Optional[tuple[str, ...]] = None
    kerberos_auth: Optional[str] = None
    kerberos_cache: Optional[str] = None
    kerberos_delegate: Optional[bool] = None
    kerberos_force_initiate: Optional[bool] = None
    kerberos_hostname: Optional[str] = None
    kerberos_keytab: Optional[str] = None
    kerberos_principal: Optional[str] = None
    log_requests: Optional[bool] = None
    metric_patterns: Optional[MetricPatterns] = None
    metrics: Optional[tuple[Union[str, MappingProxyType[str, Union[str, Metrics]]], ...]] = None
    min_collection_interval: Optional[float] = None
    namespace: Optional[str] = Field(None, pattern='\\w*')
    non_cumulative_histogram_buckets: Optional[bool] = None
    ntlm_domain: Optional[str] = None
    openmetrics_endpoint: str
    password: Optional[str] = None
    persist_connections: Optional[bool] = None
    proxy: Optional[Proxy] = None
    raw_line_filters: Optional[tuple[str, ...]] = None
    raw_metric_prefix: Optional[str] = None
    read_timeout: Optional[float] = None
    rename_labels: Optional[MappingProxyType[str, Any]] = None
    request_size: Optional[float] = None
    service: Optional[str] = None
    share_labels: Optional[MappingProxyType[str, Union[bool, ShareLabels]]] = None
    skip_proxy: Optional[bool] = None
    tag_by_endpoint: Optional[bool] = None
    tags: Optional[tuple[str, ...]] = None
    telemetry: Optional[bool] = None
    timeout: Optional[float] = None
    tls_ca_cert: Optional[str] = None
    tls_cert: Optional[str] = None
    tls_ignore_warning: Optional[bool] = None
    tls_private_key: Optional[str] = None
    tls_protocols_allowed: Optional[tuple[str, ...]] = None
    tls_use_host_header: Optional[bool] = None
    tls_verify: Optional[bool] = None
    use_latest_spec: Optional[bool] = None
    use_legacy_auth_encoding: Optional[bool] = None
    use_process_start_time: Optional[bool] = None
    username: Optional[str] = None
    weaviate_api_endpoint: Optional[str] = None

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
