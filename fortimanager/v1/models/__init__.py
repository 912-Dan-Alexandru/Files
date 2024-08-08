"""
Export FortiManager Models
"""

from .fortimanager_adom import FortiManagerADOMV1
from .fortimanager_device import FortiManagerDeviceV1, FortiManagerModifyDeviceV1
from .fortimanager_device_group import FortiManagerDeviceGroupV1
from .fortimanager_dns import (
    FortiManagerDeviceSystemDnsV1,
    FortiManagerModifyDeviceSystemDnsV1,
)
from .fortimanager_interface import FortiManagerVlanInterfaceV1
from .fortimanager_msp import FortiManagerMSPV1
from .fortimanager_template_groups import TemplateGroup, TemplateScopeMember

__all__ = [
    "FortiManagerADOMV1",
    "FortiManagerDeviceGroupV1",
    "FortiManagerDeviceV1",
    "FortiManagerModifyDeviceV1",
    "FortiManagerMSPV1",
    "TemplateGroup",
    "TemplateScopeMember",
    "FortiManagerDeviceSystemDnsV1",
    "FortiManagerModifyDeviceSystemDnsV1",
    "FortiManagerVlanInterfaceV1",
]
