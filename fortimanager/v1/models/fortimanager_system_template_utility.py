"""
Utility classes used managing complex workflows like
Fortinet System Templates
"""

from dataclasses import dataclass
from typing import Any, TypeVar

from pydantic import BaseModel, validator

from common.builders.fortimanager import (
    DeviceSystemDnsModifyRequestBuilder,
    FortinetDnsServiceBuilder,
)
from common.builders.inventory_builder import ServiceInstanceBuilder
from common.models.enums import FortiManagerServiceType
from common.southbound.fortimanager.v1.models.fortimanager_dns import (
    FortiManagerDeviceSystemDnsV1,
    FortiManagerModifyDeviceSystemDnsV1,
)
from common.southbound.fortimanager.v1.models.fortimanager_interface import (
    SystemInterface,
)

# Other configurations types types will be added when new configuration services and
# their reference models will be available. As for 26/04/2024 the only available service
# for the System templates configuration is the DNS option.

SystemTemplatesConfigurations = TypeVar(
    "SystemTemplatesConfigurations",
    FortiManagerModifyDeviceSystemDnsV1,
    FortiManagerDeviceSystemDnsV1,
    SystemInterface,
)


# pylint: disable=no-self-argument
class InternalManagementClasses(BaseModel, arbitrary_types_allowed=True):
    """
    Classes that based on a System Template widget type,
    ASSUMING THAT THE SERVICE IS AVAILABLE INTERNALLY, describes which classes
    internally handles all the aspects of the Service build phases.
    """

    service_type: FortiManagerServiceType
    service_builder_class: type[ServiceInstanceBuilder]
    create_builder: Any
    update_builder: Any

    @validator("create_builder,update_builder", check_fields=False)
    def validate_has_build_method(cls, value):
        """
        Custom validator
        """
        if not hasattr(value, "build") or not callable(getattr(value, "build")):
            raise ValueError('The assigned value must have a "build" method.')
        return value


@dataclass
class SystemTemplateConfigurationInternalMapper:
    """
    Main mapper between a System Template enabled widget/configuration option
    and classes that Harlock uses to manages the Service type associated with that
    particular configuration.
    Used mainly for dynamic processing of a System Templates configurations during
    the inventory synchronization by the Celery tasks or within the TMF 641
    workflow files.
    """

    dns = InternalManagementClasses(
        service_type=FortiManagerServiceType.DEVICE_SYSTEM_DNS,
        service_builder_class=FortinetDnsServiceBuilder,  # type: ignore
        create_builder=DeviceSystemDnsModifyRequestBuilder,
    )
