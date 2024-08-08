"""
Generated using datamodel-codegen
Meraki Device
"""

from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class MerakiDevices(str, Enum):
    """prefixes for meraki devices"""

    SWITCH = "MS"
    CELLULAR_GATEWAY = "MG"


class BeaconIdParams(BaseModel):
    """
    Bluetooth Beacons
    https://developer.cisco.com/meraki/scanning-api/#!bluetooth-beaconing-introduction
    """

    uuid: Optional[str] = None
    major: Optional[int] = None
    minor: Optional[int] = None


class BaseDevice(BaseModel):
    """
    Base class for Devices
    Common fields for all responses
    """

    serial: str
    networkId: str
    name: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    mac: Optional[str] = None
    address: Optional[str] = None
    lanIp: Optional[Optional[str]] = None
    model: Optional[str] = None
    firmware: Optional[str] = None


class DeviceBySerial(BaseDevice):
    """
    Device by serial model
    """

    notes: Optional[str] = None
    tags: List[str]
    beaconIdParams: Optional[BeaconIdParams] = None
    floorPlanId: Optional[str] = None
    wan1Ip: Optional[str] = None
    wan2Ip: Optional[Optional[str]] = None


class OrganizationDevice(BaseDevice):
    """
    This Model is seen with:
    /organizations/{organizationId}/devices
    organizations.getOrganizationDevices
    """

    notes: Optional[str] = None
    url: Optional[str] = None
    tags: Optional[List[str]] = None
    productType: Optional[str] = None
    configurationUpdatedAt: Optional[str] = None
    imei: Optional[str] = None
    wan1Ip: Optional[str] = None
    wan2Ip: Optional[Optional[str]] = None


class NetworkDevice(BaseDevice):
    """
    This model is seen with:
    /networks/{networkId}/devices
    networks.getNetworkDevices
    """

    url: Optional[str] = None
    tags: Optional[List[str]] = None
    switchProfileId: Optional[Any] = None
    floorPlanId: Optional[str] = None


class WanOptions(str, Enum):
    """
    Possible options for WanEnabled
    """

    ENABLED = "enabled"
    DISABLED = "disabled"
    NOT_CONFIGURED = "not configured"


class Wan(BaseModel):
    """
    Wan model for DeviceManagementInterfaces
    """

    wan_enabled: WanOptions | None = Field(alias="wanEnabled", default=None)
    using_static_ip: bool | None = Field(
        default=None, description="usingStaticIp", alias="usingStaticIp"
    )
    vlan: Optional[int] = None
    static_ip: str | None = Field(
        default=None, description="Static IP", alias="staticIp"
    )
    static_subnet_mask: str | None = Field(
        default=None, description="Static subnet mask", alias="staticSubnetMask"
    )
    static_gateway_ip: str | None = Field(
        default=None, description="Static Gateway IP", alias="staticGatewayIp"
    )
    static_dns: List[str] | None = Field(
        default=None, description="Static DNS", alias="staticDns"
    )


class DdnsHostnames(BaseModel):
    """
    DdnsHostnames model for DeviceManagementInterfaces

    """

    activeDdnsHostname: Optional[str] = None
    ddnsHostnameWan1: Optional[str] = None
    ddnsHostnameWan2: Optional[str] = None


class DeviceManagementInterfaces(BaseModel):
    """
    DeviceManagementInterfaces model
    """

    wan1: Optional[Wan] = None
    wan2: Optional[Wan] = None
    ddnsHostnames: Optional[DdnsHostnames] = None


class UpdateDeviceData(BaseModel):
    """
    Payload for devices.update_device
    """

    name: Optional[str] = None
    tags: Optional[List[str]] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    address: Optional[str] = None
    notes: Optional[str] = None
    moveMapMarker: Optional[bool] = None
    switchProfileId: Optional[str] = None
    floorPlanId: Optional[str] = None


class VMXSizes(Enum):
    """
    VMX Sizes
    """

    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    ONE_HUNDRED = "100"


class Profile(BaseModel):
    """
    Profile object
    """

    id: str
    iname: str
    enabled: bool


class UpdateSwitchPortData(BaseModel):
    """
    Update for switch port
    """

    name: str | None = None
    tags: List[str] | None = None
    enabled: bool | None = None
    type: str | None = None
    allowed_vlans: str | None = Field(default=None, alias="allowedVlans")
    vlan: int | None = None
    voiceVlan: int | None = None

    accessPolicyType: str | None = None
    accessPolicyNumber: int | None = None
    stickyMacAllowListLimit: int | None = None
    macAllowList: List[str] | None = None
    stickyMacAllowList: List[str] | None = None

    linkNegotiation: str | None = None
    portScheduleId: str | None = None
    stpGuard: str | None = None
    udld: str | None = None
    rstp_enabled: bool | None = Field(alias="rstpEnabled", default=None)


class SwitchPort(UpdateSwitchPortData):
    """
    Switch port informations
    """

    portId: str
