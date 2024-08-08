"""
Common Velocloud configuration modules properties and entities
"""

from enum import Enum

from pydantic import BaseModel, Field


class Cloud(str, Enum):
    ZSCALER_NET = "zscaler.net"
    ZSCALERONE_NET = "zscalerone.net"
    ZSCALERTWO_NET = "zscalertwo.net"
    ZSCALERTHREE_NET = "zscalerthree.net"
    ZSCALERBETA_NET = "zscalerbeta.net"
    ZSCLOUD_NET = "zscloud.net"
    ZSDEVEL_NET = "zsdevel.net"


class Ref(str, Enum):
    DEVICE_SETTINGS_AUTHENTICATION = "deviceSettings:authentication"
    DEVICE_SETTINGS_CSS_PROVIDER = "deviceSettings:css:provider"
    DEVICE_SETTINGS_SECURE_ACCESS_PROVIDER = "deviceSettings:secureAccess:provider"
    DEVICE_SETTINGS_EDGE_DIRECT_NVS_PROVIDER = "deviceSettings:edgeDirectNvs:provider"
    DEVICE_SETTINGS_DNS_PRIMARY_PROVIDER = "deviceSettings:dns:primaryProvider"
    DEVICE_SETTINGS_DNS_BACKUP_PROVIDER = "deviceSettings:dns:backupProvider"
    DEVICE_SETTINGS_DNS_PRIVATE_PROVIDERS = "deviceSettings:dns:privateProviders"
    DEVICE_SETTINGS_VPN_DATA_CENTER = "deviceSettings:vpn:dataCenter"
    DEVICE_SETTINGS_VPN_EDGE_HUB = "deviceSettings:vpn:edgeHub"
    DEVICE_SETTINGS_TACACS = "deviceSettings:tacacs"


class DeviceSettingsStaticRoute(BaseModel):
    destination: str | None = None
    netmask: str | None = None
    source_ip: str | None = Field(None, alias="sourceIp")
    gateway: str | None = None
    cost: int | None = None
    preferred: bool | None = None
    description: str | None = None
    cidr_prefix: str | None = Field(None, alias="cidrPrefix")
    wan_interface: str | None = Field(None, alias="wanInterface")
    icmp_probe_logical_id: str | None = Field(None, alias="icmpProbeLogicalId")
    vlan_id: int | None = Field(None, alias="vlanId")
    advertise: bool | None = None
    subinterface_id: int | None = Field(None, alias="subinterfaceId")


class NvsFromEdgeSiteData(BaseModel):
    pass
