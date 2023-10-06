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


class Projects(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, MappingProxyType[str, Any]], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of clusters to be processed.\n')


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        arbitrary_types_allowed=True,
        frozen=True,
    )
    collect_hypervisor_load: Optional[bool] = None
    collect_hypervisor_metrics: Optional[bool] = None
    collect_network_metrics: Optional[bool] = None
    collect_project_metrics: Optional[bool] = None
    collect_server_diagnostic_metrics: Optional[bool] = None
    collect_server_flavor_metrics: Optional[bool] = None
    exclude_network_ids: Optional[tuple[str, ...]] = None
    exclude_server_ids: Optional[tuple[str, ...]] = None
    keystone_server_url: Optional[str] = None
    openstack_cloud_name: Optional[str] = None
    openstack_config_file_path: Optional[str] = None
    paginated_limit: Optional[int] = None
    projects: Optional[Projects] = None
    use_agent_proxy: Optional[bool] = None
    use_shortname: Optional[bool] = None
    user: Optional[MappingProxyType[str, Any]] = None

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
