"""
Velocloud configuration/profile edge device settings module model
"""
# pylint: disable=missing-docstring
# pylint: disable=line-too-long
from __future__ import annotations
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

from common.southbound.velocloud.v1.models.profiles.common_modules_entities import (
    DeviceSettingsStaticRoute,
)
from common.southbound.velocloud.v1.models.profiles.network_device_settings import (
    L2,
    BackupProvider,
    Collector,
    InboundRouteLearning,
    OutboundRouteAdvertisement,
    PrimaryProvider,
    PrivateProviders,
    Rpf,
    User,
)


class DhcpRelay(BaseModel):
    servers: list[str] | None = None
    source_from_secondary_ip: bool | None = Field(None, alias="sourceFromSecondaryIp")


class Dhcp1(BaseModel):
    enabled: bool | None = None
    lease_time_seconds: int | None = Field(None, alias="leaseTimeSeconds")
    override: bool | None = None
    dhcp_relay: DhcpRelay | None = Field(None, alias="dhcpRelay")


class Addressing(BaseModel):
    type: str | None = None
    cidr_ip: str | None = Field(None, alias="cidrIp")
    cidr_prefix: int | None = Field(None, alias="cidrPrefix")
    netmask: str | None = None
    interface_address: str | None = Field(None, alias="interfaceAddress")
    tag: str | None = None
    tag_logical_id: str | None = Field(None, alias="tagLogicalId")


class DeviceSettingsDhcpRelay(BaseModel):
    enabled: bool | None = None
    servers: list[str] | None = None
    source_from_secondary_ip: bool | None = Field(None, alias="sourceFromSecondaryIp")


class MetaData(BaseModel):
    data_type: str | None = Field(None, alias="dataType")
    description: str | None = None
    display: bool | None = None
    list: bool | None = None
    name: str | None = None
    option: int | None = None


class DeviceSettingsDhcpOption(BaseModel):
    option: int | None = None
    value: str | None = None
    type: str | None = None
    meta_data: MetaData | None = Field(None, alias="metaData")


class DeviceSettingsFixedIp(BaseModel):
    mac_address: str | None = Field(None, alias="macAddress")
    lan_ip: str | None = Field(None, alias="lanIp")
    description: str | None = None


class DeviceSettingsDhcpV6PrefixDelegationPool(BaseModel):
    poolname: str | None = None
    prefix: str | None = None
    prefix_len: int | None = Field(None, alias="prefixLen")
    target_prefix_len: int | None = Field(None, alias="targetPrefixLen")


class PrefixDelegation(BaseModel):
    enabled: bool | None = None
    pdlist: list[DeviceSettingsDhcpV6PrefixDelegationPool] | None = None


class DeviceSettingsDhcpV6(BaseModel):
    enabled: bool | None = None
    dhcp_relay: DeviceSettingsDhcpRelay | None = Field(None, alias="dhcpRelay")
    lease_time_seconds: int | None = Field(None, alias="leaseTimeSeconds")
    options: list[DeviceSettingsDhcpOption] | None = None
    prefix_delegation: PrefixDelegation | None = Field(None, alias="prefixDelegation")
    base_dhcp_addr: int | None = Field(None, alias="baseDhcpAddr")
    num_dhcp_addr: int | None = Field(None, alias="numDhcpAddr")
    static_reserved: int | None = Field(None, alias="staticReserved")
    fixed_ip: list[DeviceSettingsFixedIp] | None = Field(None, alias="fixedIp")


class DeviceSettingsRouterAdvertisementHostSettings(BaseModel):
    mtu: bool
    default_routes: bool = Field(..., alias="defaultRoutes")
    specific_routes: bool = Field(..., alias="specificRoutes")
    nd6_timers: bool = Field(..., alias="nd6Timers")


class V6Detail(BaseModel):
    override: bool | None = None
    advertise: bool | None = None
    addressing: Addressing | None = None
    dhcp_server: DeviceSettingsDhcpV6 | None = Field(None, alias="dhcpServer")
    router_advertisement_host_settings: DeviceSettingsRouterAdvertisementHostSettings | None = Field(
        None, alias="routerAdvertisementHostSettings"
    )


class Addressing1(BaseModel):
    cidr_ip: str | None = Field(None, alias="cidrIp")
    cidr_prefix: float | None = Field(None, alias="cidrPrefix")
    netmask: str | None = None


class SecondaryIpItem(BaseModel):
    advertise: bool | None = None
    override: bool | None = None
    ping_response: bool | None = Field(None, alias="pingResponse")
    addressing: Addressing1 | None = None


class Network1(BaseModel):
    space: str | None = None
    guest: bool | None = None
    secure: bool | None = None
    advertise: bool | None = None
    ping_response: bool | None = Field(True, alias="pingResponse")
    dns_proxy: bool | None = Field(True, alias="dnsProxy")
    cost: int | None = None
    dhcp: Dhcp1 | None = None
    static_reserved: int | None = Field(None, alias="staticReserved")
    netmask: str | None = None
    cidr_prefix: int | None = Field(None, alias="cidrPrefix")
    cidr_ip: str | None = Field(None, alias="cidrIp")
    base_dhcp_addr: int | None = Field(None, alias="baseDhcpAddr")
    num_dhcp_addr: int | None = Field(None, alias="numDhcpAddr")
    name: str | None = None
    interfaces: list[str] | None = None
    vlan_id: int | None = Field(None, alias="vlanId")
    management_ip: str | None = Field(None, alias="managementIp")
    disabled: bool | None = None
    disable_v4: bool | None = Field(None, alias="disableV4")
    disable_v6: bool | None = Field(None, alias="disableV6")
    v6_detail: V6Detail | None = Field(None, alias="v6Detail")
    secondary_ip: list[SecondaryIpItem] | None = Field(None, alias="secondaryIp")


class Lan(BaseModel):
    networks: list[Network1] | None = None


class Value1(BaseModel):
    type: str | None = None
    value: str | None = None


class Action6(BaseModel):
    type: str | None = None
    values: list[Value1] | None = None


class Match2(BaseModel):
    exact_match: bool | None = Field(None, alias="exactMatch")
    type: str | None = None
    value: str | None = None


class BgpFilterRule(BaseModel):
    action: Action6 | None = None
    match: Match2 | None = None


class Filter(BaseModel):
    id: str | None = None
    name: str | None = None
    rules: list[BgpFilterRule] | None = None


class NeighborTag(str, Enum):
    UPLINK = "UPLINK"


class ConfigEdgeBgpFilterSet(BaseModel):
    ids: list[str] | None = None


class ConfigEdgeBgpNeighbor(BaseModel):
    neighbor_as: str | None = Field(None, alias="neighborAS")
    neighbor_ip: str | None = Field(None, alias="neighborIp")
    neighbor_tag: NeighborTag | None = Field(None, alias="neighborTag")
    inbound_filter: ConfigEdgeBgpFilterSet | None = Field(None, alias="inboundFilter")
    outbound_filter: ConfigEdgeBgpFilterSet | None = Field(None, alias="outboundFilter")
    allow_as: bool | None = Field(None, alias="allowAS")
    connect: str | None = None
    default_route: bool | None = Field(None, alias="defaultRoute")
    holdtime: str | None = None
    keepalive: str | None = None
    enable_md5: bool | None = Field(None, alias="enableMd5")
    md5_password: str | None = Field(None, alias="md5Password")


class Network(BaseModel):
    cidr_ip: str | None = Field(None, alias="cidrIp")
    cidr_prefix: int | None = Field(None, alias="cidrPrefix")


class Bgp1(BaseModel):
    asn: str | None = Field(None, alias="ASN")
    connected_routes: bool | None = Field(None, alias="connectedRoutes")
    disable_as_path_carry_over: bool | None = Field(
        None, alias="disableASPathCarryOver"
    )
    enabled: bool | None = None
    filters: list[Filter] | None = None
    holdtime: str | None = None
    keepalive: str | None = None
    neighbors: list[ConfigEdgeBgpNeighbor] | None = None
    networks: list[Network] | None = None
    overlay_prefix: bool | None = Field(None, alias="overlayPrefix")
    propagate_uplink: bool | None = Field(None, alias="propagateUplink")
    router_id: str | None = Field(None, alias="routerId")
    uplink_community: int | None = Field(None, alias="uplinkCommunity")


class Type6(str, Enum):
    DHCP = "DHCP"
    STATIC = "STATIC"
    PPPOE = "PPPOE"


class Addressing3(BaseModel):
    cidr_ip: str | None = Field(None, alias="cidrIp")
    cidr_prefix: int | None = Field(None, alias="cidrPrefix")
    gateway: str | None = None
    netmask: str | None = None
    type: Type6 | None = None
    username: str | None = None
    password: str | None = None


class Option(BaseModel):
    option: int | None = None
    value: str | None = None
    type: str | None = None
    meta_data: MetaData | None = Field(None, alias="metaData")


class EdgeDeviceSettingsDataDhcpServer(BaseModel):
    base_dhcp_addr: int | None = Field(None, alias="baseDhcpAddr")
    enabled: bool | None = None
    lease_time_seconds: int | None = Field(None, alias="leaseTimeSeconds")
    dhcp_relay: DhcpRelay | None = Field(None, alias="dhcpRelay")
    num_dhcp_addr: int | None = Field(None, alias="numDhcpAddr")
    static_reserved: int | None = Field(None, alias="staticReserved")
    options: list[Option] | None = None


class Ospf(BaseModel):
    area: str | None = None
    authentication: bool | None = None
    auth_id: int | None = Field(None, alias="authId")
    auth_passphrase: str | None = Field(None, alias="authPassphrase")
    cost: int | None = None
    dead_timer: int | None = Field(None, alias="deadTimer")
    mode: str | None = None
    enabled: bool | None = None
    hello_timer: int | None = Field(None, alias="helloTimer")
    inbound_route_learning: InboundRouteLearning | None = Field(
        None, alias="inboundRouteLearning"
    )
    md5_authentication: bool | None = Field(None, alias="md5Authentication")
    mtu: int | None = Field(None, alias="MTU")
    outbound_route_advertisement: OutboundRouteAdvertisement | None = Field(
        None, alias="outboundRouteAdvertisement"
    )
    passive: bool | None = None
    vlan_id: int | None = Field(None, alias="vlanId")


class Subinterface(BaseModel):
    addressing: Addressing3 | None = None
    advertise: bool | None = None
    ping_response: bool | None = Field(True, alias="pingResponse")
    dhcp_server: EdgeDeviceSettingsDataDhcpServer | None = Field(
        None, alias="dhcpServer"
    )
    disabled: bool | None = None
    nat_direct: bool | None = Field(None, alias="natDirect")
    ospf: Ospf | None = None
    override: bool | None = None
    subinterface_id: int | None = Field(None, alias="subinterfaceId")
    subinterface_type: str | None = Field(None, alias="subinterfaceType")
    vlan_id: int | None = Field(None, alias="vlanId")
    trusted: bool | None = None
    rpf: Rpf | None = None


class Addressing2(BaseModel):
    type: Type6 | None = None
    cidr_prefix: int | None = Field(None, alias="cidrPrefix")
    cidr_ip: str | None = Field(None, alias="cidrIp")
    netmask: str | None = None
    gateway: str | None = None
    username: str | None = None
    password: str | None = None


class WanOverlay(str, Enum):
    DISABLED = "DISABLED"
    AUTO_DISCOVERED = "AUTO_DISCOVERED"
    USER_DEFINED = "USER_DEFINED"


class RoutedInterface(BaseModel):
    addressing: Addressing2 | None = None
    advertise: bool | None = None
    ping_response: bool | None = Field(True, alias="pingResponse")
    dns_proxy: bool | None = Field(False, alias="dnsProxy")
    evdsl_modem_attached: bool | None = Field(False, alias="evdslModemAttached")
    disabled: bool | None = None
    dhcp_server: EdgeDeviceSettingsDataDhcpServer | None = Field(
        None, alias="dhcpServer"
    )
    encrypt_overlay: bool | None = Field(None, alias="encryptOverlay")
    l2: L2 | None = None
    name: str | None = None
    nat_direct: bool | None = Field(None, alias="natDirect")
    ospf: Ospf | None = None
    override: bool | None = None
    subinterfaces: list[Subinterface] | None = None
    vlan_id: int | None = Field(None, alias="vlanId")
    """
    static only
    """
    wan_overlay: WanOverlay | None = Field(None, alias="wanOverlay")
    trusted: bool | None = None
    rpf: Rpf | None = None
    underlay_accounting: bool | None = Field(True, alias="underlayAccounting")


class Routes(BaseModel):
    icmp_probes: list[dict[str, Any]] | None = Field(None, alias="icmpProbes")
    icmp_responders: list[dict[str, Any]] | None = Field(None, alias="icmpResponders")
    static: list[DeviceSettingsStaticRoute] | None = None
    static_v6: list[DeviceSettingsStaticRoute] | None = Field(None, alias="staticV6")


class Node(BaseModel):
    serial_number: str | None = Field(None, alias="serialNumber")
    instance_id: int | None = Field(None, alias="instanceId")


class Ha(BaseModel):
    enabled: bool | None = None
    interface: str | None = None
    vmacoverride: bool | None = None
    nodes: list[Node] | None = None
    ha_graceful_switchover: bool | None = Field(None, alias="haGracefulSwitchover")
    ha_failover_count: float | None = Field(None, alias="haFailoverCount")


class Dns1(BaseModel):
    primary_provider: PrimaryProvider | None = Field(None, alias="primaryProvider")
    backup_provider: BackupProvider | None = Field(None, alias="backupProvider")
    private_providers: PrivateProviders | None = Field(None, alias="privateProviders")


class Netflow(BaseModel):
    enable: bool | None = None
    enabled: bool | None = None
    version: int | None = None
    collectors: list[Collector] | None = None


class Vqm(BaseModel):
    enable: bool | None = None
    enabled: bool | None = None
    protocol: str | None = None
    collectors: list[Collector] | None = None


class Datum(BaseModel):
    cidr_ip: str | None = Field(None, alias="cidrIp")
    interface: str | None = None
    interval: int | None = None
    preempt: bool | None = None
    preempt_delay: int | None = Field(None, alias="preemptDelay")
    priority: int | None = None
    subinterface_id: int | None = Field(None, alias="subinterfaceId")
    vlan_id: int | None = Field(None, alias="vlanId")
    vrid: int | None = None


class Vrrp(BaseModel):
    enabled: bool | None = None
    data: list[Datum] | None = None


class Snmpv3(BaseModel):
    enabled: bool | None = None
    enable: bool | None = None
    users: list[User] | None = None


class Snmpv2c(BaseModel):
    enable: bool | None = None
    enabled: bool | None = None
    community: str | None = None
    community_list: list[str] | None = Field(None, alias="communityList")
    allowed_ip: list[str] | None = Field(None, alias="allowedIp")


class Snmp1(BaseModel):
    port: int | None = None
    snmpv2c: Snmpv2c | None = None
    snmpv3: Snmpv3 | None = None


class MultiSourceQos(BaseModel):
    enable: bool | None = None
    enabled: bool | None = None
    high_ratio: int | None = Field(None, alias="highRatio")
    normal_ratio: int | None = Field(None, alias="normalRatio")
    low_ratio: int | None = Field(None, alias="lowRatio")
    max_cap_threshold: int | None = Field(None, alias="maxCapThreshold")
    min_cap_threshold: int | None = Field(None, alias="minCapThreshold")


class Tacacs(BaseModel):
    ref: str | None = None
    source_interface: str | None = Field(None, alias="sourceInterface")


class EdgeDeviceSettingsData(BaseModel):
    bgp: Bgp1 | None = None
    dns: Dns1 | None = None
    ha: Ha | None = None
    lan: Lan | None = None
    multi_source_qos: MultiSourceQos | None = Field(None, alias="multiSourceQos")
    netflow: Netflow | None = None
    routed_interfaces: list[RoutedInterface] | None = Field(
        None, alias="routedInterfaces"
    )
    routes: Routes | None = None
    snmp: Snmp1 | None = None
    tacacs: Tacacs | None = None
    vqm: Vqm | None = None
    vrrp: Vrrp
