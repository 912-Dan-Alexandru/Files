"""
Velocloud VLAN models
"""

from __future__ import annotations
from enum import IntEnum
from typing import Any

from pydantic import BaseModel, Field


class FixedIpItem(BaseModel):
    """
    device_settings_fixed_ip
    """

    macAddress: str
    lanIp: str
    description: str


class DhcpRelay(BaseModel):
    """
    device_settings_dhcp_relay
    """

    enabled: bool
    servers: list[str]
    sourceFromSecondaryIp: bool


class MetaData(BaseModel):
    """
    device_settings_dhcp_option -> metaData
    """

    option: int
    name: str
    description: str
    dataType: str
    list: bool
    display: bool


class Option(BaseModel):
    """
    device_settings_dhcp_option
    """

    option: int
    value: str | list[str]
    type: str
    metaData: MetaData


class LeaseTimeEnum(IntEnum):
    """
    Lease Time seconds should be one of the following:
    [ 900, 3600, 14400, 43200, 86400, 604800]
    """

    LT_15_MINUTES = 900
    LT_1_HOUR = 3600
    LT_4_HOURS = 14400
    LT_12_HOURS = 43200
    LT_1_DAY = 86400
    LT_7_DAYS = 604800


class Dhcp(BaseModel):
    """
    device_settings_dhcp
    """

    # Mandatory Parameters
    leaseTimeSeconds: LeaseTimeEnum = LeaseTimeEnum.LT_1_DAY

    # Optional Parameters
    enabled: bool | None = None
    dhcpRelay: DhcpRelay | None = None
    options: list[Option] | None = None


class Addressing(BaseModel):
    """
    device_settings_lan_network -> v6Detail -> addressing
    """

    cidrIp: str | None = None
    cidrPrefix: int
    netmask: str
    type: str | None = None


class PrefixDelegationPool(BaseModel):
    """
    device_settings_dhcp_v6_prefix_delegation_pool
    """

    poolname: str
    prefix: str
    prefixLen: int
    targetPrefixLen: int


class PrefixDelegation(BaseModel):
    """
    device_settings_dhcp_v6 -> prefixDelegation
    """

    enabled: bool
    pdlist: list[PrefixDelegationPool]


class DhcpServer(BaseModel):
    """
    device_settings_dhcp_v6
    """

    leaseTimeSeconds: int
    enabled: bool | None = None
    options: list[Option] | None = None
    prefixDelegation: PrefixDelegation | None = None
    baseDhcpAddr: int | None = None
    numDhcpAddr: int | None = None
    staticReserved: int | None = None
    fixedIp: list | FixedIpItem | None = None


class Ospf(BaseModel):
    """
    device_settings_lan_network -> ospf
    """

    enabled: bool
    area: str | None = None
    passiveInterface: bool | None = None


class RouterAdvertisementHostSettings(BaseModel):
    """
    device_settings_router_advertisement_host_settings
    """

    mtu: bool
    defaultRoutes: bool
    specificRoutes: bool
    nd6Timers: bool


class V6Detail(BaseModel):
    """
    device_settings_lan_network -> v6Detail
    """

    dhcpServer: DhcpServer
    advertise: bool | None = None
    bindEdgeAddress: bool | None = None
    addressing: Addressing | None = None
    ospf: Ospf | None = None
    override: bool | None = None
    routerAdvertisementHostSettings: RouterAdvertisementHostSettings | None = None


class MacBypass(BaseModel):
    """
    device_settings_lan_network -> radiusAuthentication -> macBypass
    """

    address: str
    description: str


class RadiusAuthentication(BaseModel):
    """
    device_settings_lan_network -> radiusAuthentication
    """

    enabled: bool
    macBypass: list[MacBypass]
    aclCheck: bool


class Igmp(BaseModel):
    """
    device_settings_lan_network -> multicast -> igmp
    """

    enabled: bool
    type: str


class Pim(BaseModel):
    """
    device_settings_lan_network -> multicast -> pim
    """

    enabled: bool
    type: str


class Multicast(BaseModel):
    """
    device_settings_lan_network -> multicast
    """

    igmp: Igmp
    pim: Pim
    pimHelloTimerSeconds: Any
    pimKeepAliveTimerSeconds: Any
    pimPruneIntervalSeconds: Any
    igmpHostQueryIntervalSeconds: Any
    igmpMaxQueryResponse: Any


class Network(BaseModel):
    """
    device_settings_lan_network
    """

    # Mandatory Parameters
    vlanId: int = Field(description="Unique identifier for the VLAN")
    name: str = Field(description="Unique name for the VLAN")
    segmentId: int = Field(
        description="Identifier of the Profile Segment the VLAN is configured on",
    )
    numDhcpAddr: int = Field(
        description="Number of IP addresses available to the subnet in the DHCP Server",
    )
    netmask: str = Field(
        description="The Netmask for the subnet",
    )
    staticReserved: int = Field(
        description="Number of the statically reserved addresses",
    )
    baseDhcpAddr: int = Field(
        description="Less significant value of the starting DHCP address",
    )
    dhcp: Dhcp

    # Optional Parameters
    disabled: bool | None = None
    advertise: bool | None = None
    pingResponse: bool | None = None
    cost: int | None = None
    cidrIp: list[str | None] | None = None
    cidrPrefix: int | None = None
    disableV4: bool | None = None
    disableV6: bool | None = None
    dnsProxy: bool | None = None
    radiusAuthentication: RadiusAuthentication | None = None
    bindEdgeAddress: bool | None = None
    v6Detail: V6Detail | None = None
    multicast: Multicast | None = None
    vnfInsertion: list[bool | None] | None = None

    # if set "VLAN is in use in an interface" message instead of the "Del" link
    interfaces: list[str] | None = None
    override: bool | None = None
    fixedIp: list | FixedIpItem | None = None
    ospf: Ospf | None = None


class VLANs(BaseModel):
    """
    Array of device_settings_lan_network
    """

    networks: list[Network]
