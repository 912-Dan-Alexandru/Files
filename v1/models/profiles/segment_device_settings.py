"""
Velocloud profile device settings section
"""

# pylint: disable=missing-docstring
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
from __future__ import annotations
from datetime import datetime
from enum import Enum
from ipaddress import IPv4Address
from typing import Any

from pydantic import BaseModel, Field, conint, constr

from common.southbound.velocloud.v1.models.profiles.common_modules_entities import (
    Cloud,
    DeviceSettingsStaticRoute,
    NvsFromEdgeSiteData,
    Ref,
)
from common.southbound.velocloud.v1.models.profiles.edge_device_settings import (
    DeviceSettingsDhcpOption,
    DeviceSettingsDhcpRelay,
    DeviceSettingsDhcpV6,
    DeviceSettingsFixedIp,
    DeviceSettingsRouterAdvertisementHostSettings,
    NeighborTag,
    Node,
    Rpf,
    WanOverlay,
)
from common.southbound.velocloud.v1.models.profiles.network_device_settings import (
    DeviceSettingsGlobalIPv6Settings,
    DeviceSettingsSnmpv2c,
    DeviceSettingsVpnHub,
    LogicalidReference,
)


class DeviceSettingsBfdRule(BaseModel):
    peer_address: str | None = Field(None, alias="peerAddress")
    local_address: str | None = Field(None, alias="localAddress")
    multihop: bool | None = None
    detect_multiplier: int | None = Field(None, alias="detectMultiplier")
    receive_interval: int | None = Field(None, alias="receiveInterval")
    transmit_interval: int | None = Field(None, alias="transmitInterval")


class DeviceSettingsBfd(BaseModel):
    enabled: bool | None = None
    override: bool | None = None
    rules: list[DeviceSettingsBfdRule] | None = None
    rules_v6: list[DeviceSettingsBfdRule] | None = Field(None, alias="rulesV6")


class Network2(str, Enum):
    ATT = "ATT"
    SPRINT = "SPRINT"
    VERIZON = "VERIZON"
    VODAFONE = "VODAFONE"
    TELSTRA = "TELSTRA"
    GENERIC = "GENERIC"
    UNKNOWN = ""


class Iptype(str, Enum):
    I_PV4 = "IPv4"
    I_PV4V6 = "IPv4v6"


class Cellular(BaseModel):
    sim_pin: str | None = Field(None, alias="simPin")
    network: Network2 | None = None
    apn: str | None = None
    iptype: Iptype | None = None
    username: str | None = None
    password: str | None = None


class DeviceSettingsHa(BaseModel):
    enabled: bool | None = None
    interface: str | None = None
    vmacoverride: bool | None = None
    nodes: list[Node] | None = None
    ha_graceful_switchover: bool | None = Field(None, alias="haGracefulSwitchover")
    ha_failover_count: float | None = Field(None, alias="haFailoverCount")


class DeviceSettingsHubInterconnect(BaseModel):
    override: bool | None = None
    enabled: bool | None = None


class DeviceSettingsHandoffGatewayIpsecDetail(BaseModel):
    ipsec_gateway_address: str | None = Field(None, alias="ipsecGatewayAddress")
    strict_host_check: bool | None = Field(None, alias="strictHostCheck")


class DeviceSettingsMacAllowlistAllowedMac(BaseModel):
    address: str
    description: str | None = None


class MacAllowlist(BaseModel):
    enabled: bool
    enable_mac_filtering_for_ap_probes: bool = Field(
        ..., alias="enableMACFilteringForAPProbes"
    )
    allowed_macs: list[DeviceSettingsMacAllowlistAllowedMac] = Field(
        ..., alias="allowedMacs"
    )


class Duplex(str, Enum):
    FULL = "FULL"
    HALF = "HALF"


class ProbeInterval(str, Enum):
    FIELD_1 = "1"
    FIELD_3 = "3"
    FIELD_5 = "5"
    FIELD_10 = "10"


class L23(BaseModel):
    autonegotiation: bool | None = None
    speed: str | None = None
    duplex: Duplex | None = None
    mtu: int | None = Field(None, alias="MTU")
    los_detection: bool | None = Field(None, alias="losDetection")
    probe_interval: ProbeInterval | None = Field(None, alias="probeInterval")


class PortMode(str, Enum):
    ACCESS = "access"
    TRUNK = "trunk"


class Type16(str, Enum):
    WIRED = "wired"
    WIRELESS = "wireless"


class AuthenticationType(str, Enum):
    NONE = "none"
    FIELD_802_1X = "802.1x"


class SecurityMode(str, Enum):
    OPEN = "Open"
    WPA2_ENTERPRISE = "WPA2Enterprise"
    WPA2_PERSONAL = "WPA2Personal"


class Type17(str, Enum):
    IGMP_V2 = "IGMP_V2"


class Igmp(BaseModel):
    enabled: bool | None = None
    type: Type17 | None = None


class Type18(str, Enum):
    PIM_SM = "PIM_SM"


class Pim(BaseModel):
    enabled: bool | None = None
    type: Type18 | None = None


class DeviceSettingsLanInterface(BaseModel):
    override: bool | None = None
    name: str | None = None
    cwp: bool | None = None
    disabled: bool | None = None
    l2: L23 | None = None
    port_mode: PortMode | None = Field(None, alias="portMode")
    space: str | None = None
    type: Type16 | None = None
    untagged_vlan: str | None = Field(None, alias="untaggedVlan")
    vlan_ids: list[int] | None = Field(None, alias="vlanIds")
    authentication_type: AuthenticationType | None = Field(
        None, alias="authenticationType"
    )
    mac_allowlist: MacAllowlist | None = Field(None, alias="macAllowlist")
    radius_acl_check: bool | None = Field(None, alias="radiusAclCheck")
    broadcast_ssid: bool | None = Field(None, alias="broadcastSsid")
    passphrase: str | None = None
    ssid: str | None = None
    security_mode: SecurityMode | None = Field(None, alias="securityMode")


class Subnet(BaseModel):
    cidr_ip: str | None = Field(None, alias="cidrIp")
    cidr_prefix: int | None = Field(None, alias="cidrPrefix")


class DeviceSettingsLanManagementTraffic(BaseModel):
    override: bool | None = None
    source_interface: str | None = Field(None, alias="sourceInterface")


class DeviceSettingsDhcp(BaseModel):
    enabled: bool | None = None
    dhcp_relay: DeviceSettingsDhcpRelay | None = Field(None, alias="dhcpRelay")
    lease_time_seconds: int | None = Field(None, alias="leaseTimeSeconds")
    base_dhcp_addr: int | None = Field(None, alias="baseDhcpAddr")
    num_dhcp_addr: int | None = Field(None, alias="numDhcpAddr")
    options: list[DeviceSettingsDhcpOption] | None = None
    override: bool | None = None


class Multicast(BaseModel):
    igmp: Igmp | None = None
    igmp_host_query_interval_seconds: int | None = Field(
        None, alias="igmpHostQueryIntervalSeconds"
    )
    igmp_max_query_response: int | None = Field(None, alias="igmpMaxQueryResponse")
    pim: Pim | None = None
    pim_hello_timer_seconds: int | None = Field(None, alias="pimHelloTimerSeconds")
    pim_keep_alive_timer_seconds: int | None = Field(
        None, alias="pimKeepAliveTimerSeconds"
    )
    pim_prune_interval_seconds: int | None = Field(
        None, alias="pimPruneIntervalSeconds"
    )


class Ospf4(BaseModel):
    enabled: bool | None = None
    override: bool | None = None
    area: str | None = None
    passive_interface: bool | None = Field(None, alias="passiveInterface")


class Addressing5(BaseModel):
    cidr_ip: str | None = Field(None, alias="cidrIp")
    cidr_prefix: int | None = Field(None, alias="cidrPrefix")
    netmask: str | None = None
    type: str | None = None
    interface_address: str | None = Field(None, alias="interfaceAddress")
    tag: str | None = None
    tag_logical_id: str | None = Field(None, alias="tagLogicalId")


class V6Detail3(BaseModel):
    override: bool | None = None
    advertise: bool | None = None
    bind_edge_address: bool | None = Field(None, alias="bindEdgeAddress")
    addressing: Addressing5 | None = None
    dhcp_server: DeviceSettingsDhcpV6 | None = Field(None, alias="dhcpServer")
    router_advertisement_host_settings: (
        DeviceSettingsRouterAdvertisementHostSettings | None
    ) = Field(None, alias="routerAdvertisementHostSettings")
    ospf: Ospf4 | None = None


class MacBypas(BaseModel):
    address: str | None = None
    description: str | None = None


class RadiusAuthentication(BaseModel):
    enabled: bool | None = None
    mac_bypass: list[MacBypas] | None = Field(None, alias="macBypass")
    acl_check: bool | None = Field(None, alias="aclCheck")


class DeviceSettingsLanNetwork(BaseModel):
    override: bool | None = None
    advertise: bool | None = None
    ping_response: bool | None = Field(True, alias="pingResponse")
    dns_proxy: bool | None = Field(True, alias="dnsProxy")
    bind_edge_address: bool | None = Field(None, alias="bindEdgeAddress")
    base_dhcp_addr: int | None = Field(None, alias="baseDhcpAddr")
    cidr_ip: str | None = Field(None, alias="cidrIp")
    cidr_prefix: int | None = Field(None, alias="cidrPrefix")
    cost: int | None = None
    dhcp: DeviceSettingsDhcp | None = None
    disabled: bool | None = None
    disable_v4: bool | None = Field(None, alias="disableV4")
    disable_v6: bool | None = Field(None, alias="disableV6")
    interfaces: list[str] | None = None
    multicast: Multicast | None = None
    name: str | None = None
    netmask: str | None = None
    num_dhcp_addr: int | None = Field(None, alias="numDhcpAddr")
    ospf: Ospf4 | None = None
    fixed_ip: list[DeviceSettingsFixedIp] | None = Field(None, alias="fixedIp")
    segment_id: int | None = Field(None, alias="segmentId")
    static_reserved: int | None = Field(None, alias="staticReserved")
    vlan_id: int | None = Field(None, alias="vlanId")
    vnf_insertion: bool | None = Field(None, alias="vnfInsertion")
    v6_detail: V6Detail3 | None = Field(None, alias="v6Detail")
    radius_authentication: RadiusAuthentication | None = Field(
        None, alias="radiusAuthentication"
    )


class Mode1(str, Enum):
    MAC = "MAC"
    IP = "IP"


class Visibility(BaseModel):
    override: bool | None = None
    mode: Mode1 | None = None


class DeviceSettingsLan(BaseModel):
    interfaces: list[DeviceSettingsLanInterface] | None = None
    management: Subnet | None = None
    management_traffic: DeviceSettingsLanManagementTraffic | None = Field(
        None, alias="managementTraffic"
    )
    networks: list[DeviceSettingsLanNetwork] | None = None
    visibility: Visibility | None = None


class Ospf6(BaseModel):
    enabled: bool | None = None
    area: list[str] | None = None


class V6Detail4(BaseModel):
    cidr_ip: str | None = Field(None, alias="cidrIp")
    cidr_prefix: float | None = Field(None, alias="cidrPrefix")
    advertise: bool | None = None
    ospf: Ospf6 | None = None


class DeviceSettingsLoopbackInterfaces1(BaseModel):
    cidr_ip: str | None = Field(None, alias="cidrIp")
    cidr_prefix: float | None = Field(None, alias="cidrPrefix")
    advertise: bool | None = None
    ping_response: bool | None = Field(None, alias="pingResponse")
    segment_id: float | None = Field(None, alias="segmentId")
    ospf: Ospf6 | None = None
    disable_v4: bool | None = Field(None, alias="disableV4")
    disable_v6: bool | None = Field(None, alias="disableV6")
    v6_detail: V6Detail4 | None = Field(None, alias="v6Detail")


class DeviceSettingsLoopbackInterfaces(BaseModel):
    __root__: dict[str, DeviceSettingsLoopbackInterfaces1] | None = None


class DeviceSettingsMultiSourceQos(BaseModel):
    enabled: bool | None = None
    override: bool | None = None
    high_ratio: int | None = Field(None, alias="highRatio")
    normal_ratio: int | None = Field(None, alias="normalRatio")
    low_ratio: int | None = Field(None, alias="lowRatio")
    max_cap_threshold: int | None = Field(None, alias="maxCapThreshold")
    min_cap_threshold: int | None = Field(None, alias="minCapThreshold")


class DeviceSettingsNtpServer(BaseModel):
    server: str | None = None


class DeviceSettingsNtp(BaseModel):
    source_interface: str | None = Field(None, alias="sourceInterface")
    enabled: bool | None = None
    override: bool | None = None
    servers: list[DeviceSettingsNtpServer] | None = None


class Authentication1(str, Enum):
    NONE = "NONE"
    MD5 = "MD5"


class DeviceSettingsNtpKey(BaseModel):
    key: str | None = None
    key_number: int | None = Field(None, alias="keyNumber")


class DeviceSettingsNtpAsServer(BaseModel):
    enabled: bool | None = None
    override: bool | None = None
    authentication: Authentication1 | None = None
    keys: list[DeviceSettingsNtpKey] | None = None


class DeviceSettingsRadio(BaseModel):
    band: str | None = None
    channel: str | None = None
    is_enabled: bool | None = Field(None, alias="isEnabled")
    mode: str | None = None
    name: str | None = None
    radio_id: int | None = Field(None, alias="radioId")
    width: str | None = None


class DeviceSettingsRadioSettings(BaseModel):
    country: str | None = None
    radios: list[DeviceSettingsRadio] | None = None


class DeviceSettingsL2Settings(BaseModel):
    override_arp_timeout: bool | None = Field(None, alias="overrideARPTimeout")
    arp_stale_timeout_minutes: int | None = Field(None, alias="arpStaleTimeoutMinutes")
    arp_dead_timeout_minutes: int | None = Field(None, alias="arpDeadTimeoutMinutes")
    arp_cleanup_timeout_minutes: int | None = Field(
        None, alias="arpCleanupTimeoutMinutes"
    )


class DeviceSettingsAuthentication(BaseModel):
    override: bool | None = None
    source_interface: str | None = Field(None, alias="sourceInterface")
    ref: Ref | None = None


class DefaultRoute(BaseModel):
    enabled: bool | None = None
    advertise: str | None = None


class Type8(str, Enum):
    PERMIT = "PERMIT"
    DENY = "DENY"


class Type9(str, Enum):
    AS_PATH_PREPEND = "AS_PATH_PREPEND"
    METRIC = "METRIC"
    LOCAL_PREFERENCE = "LOCAL_PREFERENCE"
    COMMUNITY = "COMMUNITY"


class Value(BaseModel):
    type: Type9 | None = None
    value: str | None = None


class Action4(BaseModel):
    type: Type8 | None = None
    values: list[Value] | None = None


class Type10(str, Enum):
    COMMUNITY = "COMMUNITY"
    PREFIX = "PREFIX"


class Match1(BaseModel):
    exact_match: bool | None = Field(None, alias="exactMatch")
    type: Type10 | None = None
    value: str | None = None


class DeviceSettingsBgpFilterRule(BaseModel):
    action: Action4 | None = None
    match: Match1 | None = None


class DeviceSettingsBgpFilter(BaseModel):
    ids: list[str] | None = None
    name: str | None = None
    rules: list[DeviceSettingsBgpFilterRule] | None = None


class DeviceSettingsBgpFilterSet(BaseModel):
    ids: list[str] | None = None


class DeviceSettingsBgpNeighbor(BaseModel):
    neighbor_as: str | None = Field(None, alias="neighborAS")
    neighbor_ip: str | None = Field(None, alias="neighborIp")
    neighbor_tag: NeighborTag | None = Field(None, alias="neighborTag")
    source_interface: str | None = Field(None, alias="sourceInterface")
    inbound_filter: DeviceSettingsBgpFilterSet | None = Field(
        None, alias="inboundFilter"
    )
    outbound_filter: DeviceSettingsBgpFilterSet | None = Field(
        None, alias="outboundFilter"
    )
    local_ip: str | None = Field(None, alias="localIp")
    max_hop: str | None = Field(None, alias="maxHop")
    allow_as: bool | None = Field(None, alias="allowAS")
    connect: str | None = None
    default_route: bool | None = Field(None, alias="defaultRoute")
    holdtime: str | None = None
    keepalive: str | None = None
    enable_md5: bool | None = Field(None, alias="enableMd5")
    md5_password: str | None = Field(None, alias="md5Password")


class DeviceSettingsBgpNetwork(BaseModel):
    cidr_ip: str | None = Field(None, alias="cidrIp")
    cidr_prefix: int | None = Field(None, alias="cidrPrefix")
    segment_id: str | None = Field(None, alias="segmentId")


class DeviceSettingsBgpOspfRedistribution(BaseModel):
    enabled: bool | None = None
    metric: int | None = None


class V6Detail1(BaseModel):
    default_route: DefaultRoute | None = Field(None, alias="defaultRoute")
    connected_routes: bool | None = Field(None, alias="connectedRoutes")
    neighbors: list[DeviceSettingsBgpNeighbor] | None = None
    networks: list[DeviceSettingsBgpNetwork] | None = None
    overlay_prefix: bool | None = Field(None, alias="overlayPrefix")
    disable_as_path_carry_over: bool | None = Field(
        None, alias="disableASPathCarryOver"
    )
    propagate_uplink: bool | None = Field(None, alias="propagateUplink")
    ospf: DeviceSettingsBgpOspfRedistribution | None = None


class DeviceSettingsBgp(BaseModel):
    enabled: bool | None = None
    override: bool | None = None
    asn: str | None = Field(None, alias="ASN")
    connected_routes: bool | None = Field(None, alias="connectedRoutes")
    default_route: DefaultRoute | None = Field(None, alias="defaultRoute")
    disable_as_path_carry_over: bool | None = Field(
        None, alias="disableASPathCarryOver"
    )
    filters: list[DeviceSettingsBgpFilter] | None = None
    holdtime: str | None = None
    enable_graceful_restart: bool | None = Field(None, alias="enableGracefulRestart")
    restarttime: str | None = None
    stalepathtime: str | None = None
    is_edge: bool | None = Field(None, alias="isEdge")
    keepalive: str | None = None
    neighbors: list[DeviceSettingsBgpNeighbor] | None = None
    networks: list[DeviceSettingsBgpNetwork] | None = None
    ospf: DeviceSettingsBgpOspfRedistribution | None = None
    overlay_prefix: bool | None = Field(None, alias="overlayPrefix")
    propagate_uplink: bool | None = Field(None, alias="propagateUplink")
    router_id: str | None = Field(None, alias="routerId")
    uplink_community: str | None = Field(None, alias="uplinkCommunity")
    v6_detail: V6Detail1 | None = Field(None, alias="v6Detail")


class TunnelingProtocol1(str, Enum):
    GRE = "GRE"
    IPSEC = "IPSEC"


class Ikeprop(BaseModel):
    protocol_version: int | None = Field(None, alias="protocolVersion")


class Greprop(BaseModel):
    keepalive_interval_secs: conint(ge=0, le=30) | None = Field(
        None, alias="keepaliveIntervalSecs"
    )
    keepalive_retries: conint(ge=0, le=10) | None = Field(
        None, alias="keepaliveRetries"
    )


class Config(BaseModel):
    tunneling_protocol: TunnelingProtocol1 | None = Field(
        None, alias="tunnelingProtocol"
    )
    authentication_algorithm: str | None = Field(None, alias="authenticationAlgorithm")
    encryption_algorithm: str | None = Field(None, alias="encryptionAlgorithm")
    redirect: str | None = None
    ikeprop: Ikeprop | None = Field(None, alias="IKEPROP")
    greprop: Greprop | None = Field(None, alias="GREPROP")


class Provider1(BaseModel):
    ref: Ref | None = None


class CloudSecurityServiceSiteData(BaseModel):
    pass


class DeviceSettingsCloudSecuritySite(BaseModel):
    data: CloudSecurityServiceSiteData | None = None
    logical_id: str | None = Field(None, alias="logicalId")


class DeviceSettingsCloudSecurity(BaseModel):
    enabled: bool | None = None
    override: bool | None = None
    config: Config | None = None
    provider: Provider1 | None = None
    sites: list[DeviceSettingsCloudSecuritySite] | None = None


class Provider2(BaseModel):
    ref: Ref | None = None
    logical_id: str | None = Field(None, alias="logicalId")


class DeviceSettingsSecureAccess(BaseModel):
    enabled: bool | None = None
    override: bool | None = None
    provider: Provider2 | None = None


class ProviderConfig(BaseModel):
    use_all_public_wan_links: bool | None = Field(None, alias="useAllPublicWanLinks")
    enabled: bool | None = None


class DeviceSettingsNvsFromEdgeSite(BaseModel):
    data: NvsFromEdgeSiteData | None = None
    logical_id: str | None = Field(None, alias="logicalId")


class Provider5(BaseModel):
    logical_id: str | None = Field(None, alias="logicalId")
    config: ProviderConfig | None = None
    sites: list[DeviceSettingsNvsFromEdgeSite] | None = None


class Provider4(BaseModel):
    ref: Ref | None = None


class DeviceSettingsNvsFromEdge(BaseModel):
    enabled: bool | None = None
    override: bool | None = None
    provider: Provider4 | None = None
    providers: list[Provider5] | None = None


class PrimaryProvider2(BaseModel):
    ref: Ref | None = None


class BackupProvider2(BaseModel):
    ref: Ref | None = None


class PrivateProviders2(BaseModel):
    ref: Ref | None = None


class LocalDn(BaseModel):
    ipv4_address: list[str] | None = Field(None, alias="ipv4Address")
    ipv6_address: list[str] | None = Field(None, alias="ipv6Address")
    fqdn: str | None = None


class DeviceSettingsDns(BaseModel):
    override: bool | None = None
    source_interface: str | None = Field(None, alias="sourceInterface")
    primary_provider: PrimaryProvider2 | None = Field(None, alias="primaryProvider")
    backup_provider: BackupProvider2 | None = Field(None, alias="backupProvider")
    private_providers: PrivateProviders2 | None = Field(None, alias="privateProviders")
    local_dns: list[LocalDn] | None = Field(None, alias="localDNS")


class DeviceSettingsHandoffGateway(LogicalidReference):
    ipsec_detail: DeviceSettingsHandoffGatewayIpsecDetail | None = Field(
        None, alias="ipsecDetail"
    )


class DeviceSettingsHandoffGateways(BaseModel):
    override: bool | None = None
    auto_select: bool | None = Field(None, alias="autoSelect")
    gateway_list: list[DeviceSettingsHandoffGateway] | None = Field(
        None, alias="gatewayList"
    )
    gateways: list[LogicalidReference] | None = None
    """
    *Deprecated* - Do not use, use gatewayList instead.
    """


class Type11(str, Enum):
    SOURCE_IP = "SOURCE_IP"


class Type12(str, Enum):
    STATIC = "STATIC"


class Type13(str, Enum):
    SOURCE = "source"
    DESTINATION = "destination"


class DeviceSettingsMulticastPimOnWanOverlay(BaseModel):
    enabled: bool | None = None
    type: Type11 | None = None
    source_cidr_ip: str | None = Field(None, alias="sourceCidrIp")
    source_interface: str | None = Field(None, alias="sourceInterface")


class DeviceSettingsMulticastRpStaticGroup(BaseModel):
    multicast_groups: list[str] | None = Field(None, alias="multicastGroups")
    rp_address: str | None = Field(None, alias="rpAddress")


class DeviceSettingsMulticastRp(BaseModel):
    type: Type12 | None = None
    static_groups: list[DeviceSettingsMulticastRpStaticGroup] | None = Field(
        None, alias="staticGroups"
    )


class DeviceSettingsMulticast(BaseModel):
    enabled: bool | None = None
    override: bool | None = None
    igmp_host_query_interval_seconds: int | None = Field(
        None, alias="igmpHostQueryIntervalSeconds"
    )
    igmp_max_query_response: int | None = Field(None, alias="igmpMaxQueryResponse")
    pim_keep_alive_timer_seconds: int | None = Field(
        None, alias="pimKeepAliveTimerSeconds"
    )
    pim_on_wan_overlay: DeviceSettingsMulticastPimOnWanOverlay | None = Field(
        None, alias="pimOnWanOverlay"
    )
    pim_prune_interval_seconds: int | None = Field(
        None, alias="pimPruneIntervalSeconds"
    )
    rp: DeviceSettingsMulticastRp | None = None


class DeviceSettingsNatRule(BaseModel):
    type: Type13
    description: str | None = None
    inside_cidr_ip: IPv4Address = Field(..., alias="insideCidrIp")
    inside_cidr_prefix: int = Field(..., alias="insideCidrPrefix")
    inside_netmask: IPv4Address = Field(..., alias="insideNetmask")
    inside_port: int | None = Field(None, alias="insidePort")
    outside_cidr_ip: IPv4Address = Field(..., alias="outsideCidrIp")
    outside_cidr_prefix: int = Field(..., alias="outsideCidrPrefix")
    outside_netmask: IPv4Address = Field(..., alias="outsideNetmask")
    outside_port: int | None = Field(None, alias="outsidePort")


class DeviceSettingsNatDualRule(BaseModel):
    description: str | None = None
    src_inside_cidr_ip: str = Field(..., alias="srcInsideCidrIp")
    src_inside_cidr_prefix: int = Field(..., alias="srcInsideCidrPrefix")
    src_inside_cidr_netmask: str = Field(..., alias="srcInsideCidrNetmask")
    src_outside_cidr_ip: str = Field(..., alias="srcOutsideCidrIp")
    src_outside_cidr_prefix: int = Field(..., alias="srcOutsideCidrPrefix")
    src_outside_cidr_netmask: str = Field(..., alias="srcOutsideCidrNetmask")
    dest_inside_cidr_ip: str = Field(..., alias="destInsideCidrIp")
    dest_inside_cidr_prefix: int = Field(..., alias="destInsideCidrPrefix")
    dest_inside_cidr_netmask: str = Field(..., alias="destInsideCidrNetmask")
    dest_outside_cidr_ip: str = Field(..., alias="destOutsideCidrIp")
    dest_outside_cidr_prefix: int = Field(..., alias="destOutsideCidrPrefix")
    dest_outside_cidr_netmask: str = Field(..., alias="destOutsideCidrNetmask")


class Intervals(BaseModel):
    flow_stats: int | None = Field(None, alias="flowStats")
    flow_link_stats: int | None = Field(None, alias="flowLinkStats")
    tunnel_stats: int | None = Field(None, alias="tunnelStats")
    vrf_table: int | None = Field(None, alias="vrfTable")
    application_table: int | None = Field(None, alias="applicationTable")
    interface_table: int | None = Field(None, alias="interfaceTable")
    link_table: int | None = Field(None, alias="linkTable")


class DeviceSettingsNat(BaseModel):
    override: bool | None = None
    rules: list[DeviceSettingsNatRule] | None = Field(None, max_items=256)
    dual_rules: list[DeviceSettingsNatDualRule] | None = Field(None, alias="dualRules")


class DeviceSettingsNetflowFilterList(BaseModel):
    type: str | None = None
    name: str | None = None
    logical_id: str | None = Field(None, alias="logicalId")


class DeviceSettingsNetflowCollector(BaseModel):
    type: str | None = None
    source_interface: str | None = Field(None, alias="sourceInterface")
    name: str | None = None
    allow_all_segment: bool | None = Field(None, alias="allowAllSegment")
    logical_id: str | None = Field(None, alias="logicalId")
    filter_list: list[DeviceSettingsNetflowFilterList] | None = Field(
        None, alias="filterList"
    )


class DeviceSettingsNetflow(BaseModel):
    enabled: bool | None = None
    override: bool | None = None
    collectors: list[DeviceSettingsNetflowCollector] | None = None
    version: int | None = None
    intervals: Intervals | None = None


class MetricType(str, Enum):
    E1 = "E1"
    E2 = "E2"


class DeviceSettingsOspfAggregation(BaseModel):
    prefix: str | None = None
    prefix_length: int | None = Field(None, alias="prefixLength")
    no_advertise: bool | None = Field(None, alias="noAdvertise")
    tag: int | None = None
    metric: int | None = None
    metric_type: MetricType | None = Field(None, alias="metricType")


class DeviceSettingsOspfArea(BaseModel):
    id: int | None = None
    name: str | None = None
    type: str | None = None


class DeviceSettingsOspfBgpRedistribution(BaseModel):
    enabled: bool | None = None
    metric: int | None = None
    metric_type: MetricType | None = Field(None, alias="metricType")


class DefaultRouteAdvertise(str, Enum):
    ALWAYS = "ALWAYS"
    CONDITIONAL = "CONDITIONAL"
    NONE = "NONE"


class DefaultRoutes(str, Enum):
    OE1 = "OE1"
    OE2 = "OE2"
    NONE = "NONE"


class V6Detail2(BaseModel):
    aggregation: list[DeviceSettingsOspfAggregation] | None = None
    enabled: bool | None = None
    areas: list[DeviceSettingsOspfArea] | None = None
    bgp: DeviceSettingsOspfBgpRedistribution | None = None
    default_prefixes: bool | None = Field(None, alias="defaultPrefixes")
    default_route_advertise: DefaultRouteAdvertise | None = Field(
        None, alias="defaultRouteAdvertise"
    )
    default_routes: DefaultRoutes | None = Field(None, alias="defaultRoutes")


class DeviceSettingsOspf(BaseModel):
    aggregation: list[DeviceSettingsOspfAggregation] | None = None
    enabled: bool | None = None
    areas: list[DeviceSettingsOspfArea] | None = None
    bgp: DeviceSettingsOspfBgpRedistribution | None = None
    default_prefixes: bool | None = Field(None, alias="defaultPrefixes")
    default_route_advertise: DefaultRouteAdvertise | None = Field(
        None, alias="defaultRouteAdvertise"
    )
    default_routes: DefaultRoutes | None = Field(None, alias="defaultRoutes")
    v6_detail: V6Detail2 | None = Field(None, alias="v6Detail")


class DeviceSettingsIcmpProbe(BaseModel):
    pass


class DeviceSettingsIcmpResponder(BaseModel):
    pass


class NsdType(str, Enum):
    NVS_VIA_EDGE_SERVICE = "nvsViaEdgeService"
    DATA_CENTER = "dataCenter"


class DeviceSettingsNsdRoute(BaseModel):
    advertise: bool | None = None
    cidr_ip: str | None = Field(None, alias="cidrIp")
    cidr_ip_end: str | None = Field(None, alias="cidrIpEnd")
    cidr_ip_start: str | None = Field(None, alias="cidrIpStart")
    cidr_prefix: str | None = Field(None, alias="cidrPrefix")
    cost: int | None = None
    destination: str | None = None
    gateway_logical_id: str | None = Field(None, alias="gatewayLogicalId")
    gateway_name: str | None = Field(None, alias="gatewayName")
    is_static: bool | None = Field(None, alias="isStatic")
    name: str | None = None
    net_mask: str | None = Field(None, alias="netMask")
    nsd: str | None = None
    nsd_logical_id: str | None = Field(None, alias="nsdLogicalId")
    nsd_type: NsdType | None = Field(None, alias="nsdType")
    preferred: bool | None = None


class Routes1(BaseModel):
    icmp_probes: list[DeviceSettingsIcmpProbe] | None = Field(None, alias="icmpProbes")
    icmp_responders: list[DeviceSettingsIcmpResponder] | None = Field(
        None, alias="icmpResponders"
    )
    nsd: list[DeviceSettingsNsdRoute] | None = None
    static: list[DeviceSettingsStaticRoute] | None = None
    static_v6: list[DeviceSettingsStaticRoute] | None = Field(None, alias="staticV6")


class DeviceSettingsSnmpv3User(BaseModel):
    name: str | None = None
    passphrase: str | None = "null"
    auth_alg: str | None = Field(None, alias="authAlg")
    privacy: bool | None = None
    authentication: bool | None = None
    encr_alg: str | None = Field(None, alias="encrAlg")


class DeviceSettingsSnmpv3(BaseModel):
    enabled: bool | None = None
    users: list[DeviceSettingsSnmpv3User] | None = None


class DeviceSettingsSnmp(BaseModel):
    override: bool | None = None
    port: int | None = None
    snmpv2c: DeviceSettingsSnmpv2c | None = None
    snmpv3: DeviceSettingsSnmpv3 | None = None


class FacilityCode(str, Enum):
    LOCAL0 = "local0"
    LOCAL1 = "local1"
    LOCAL2 = "local2"
    LOCAL3 = "local3"
    LOCAL4 = "local4"
    LOCAL5 = "local5"
    LOCAL6 = "local6"
    LOCAL7 = "local7"


class Protocol(str, Enum):
    TCP = "TCP"
    UDP = "UDP"


class Severity1(str, Enum):
    EMERG = "EMERG"
    ALERT = "ALERT"
    CRIT = "CRIT"
    ERR = "ERR"
    WARNING = "WARNING"
    NOTICE = "NOTICE"
    INFO = "INFO"
    DEBUG = "DEBUG"


class Role(str, Enum):
    EDGE_EVENT = "EDGE EVENT"
    FIREWALL_EVENT = "FIREWALL EVENT"
    EDGE_AND_FIREWALL_EVENT = "EDGE AND FIREWALL EVENT"


class DeviceSettingsSyslogCollector(BaseModel):
    host: str
    port: int
    protocol: Protocol
    roles: list[Role]
    severity: Severity1
    source_interface: str = Field(..., alias="sourceInterface")
    tag: str | None = None


class DeviceSettingsSyslog(BaseModel):
    enabled: bool
    facility_code: FacilityCode | None = Field(None, alias="facilityCode")
    override: bool | None = None
    collectors: list[DeviceSettingsSyslogCollector]


class EdgeToEdgeHub1(BaseModel):
    enabled: bool | None = None
    ref: Ref | None = None
    vpn_hubs: list[DeviceSettingsVpnHub] | None = Field(None, alias="vpnHubs")


class DeviceSettingsVpnProfileIsolation(BaseModel):
    enabled: bool | None = None


class Dynamic2(BaseModel):
    enabled: bool | None = None
    isolation: DeviceSettingsVpnProfileIsolation | None = None
    type: str | None = None
    timeout: int | None = None


class DeviceSettingsVpnProfileIsolationDeprecated(BaseModel):
    enabled: bool | None = None
    profile_logical_id: str | None = Field(None, alias="profileLogicalId")
    isolate_dynamic: bool | None = Field(None, alias="isolateDynamic")


class IsolationGroup(BaseModel):
    logical_id: str | None = Field(None, alias="logicalId")


class EdgeToEdgeDetail2(BaseModel):
    auto_select_vpn_hubs: bool | None = Field(None, alias="autoSelectVpnHubs")
    dynamic: Dynamic2 | None = None
    encryption_protocol: str | None = Field(None, alias="encryptionProtocol")
    profile_isolation: DeviceSettingsVpnProfileIsolationDeprecated | None = Field(
        None, alias="profileIsolation"
    )
    isolation: DeviceSettingsVpnProfileIsolation | None = None
    isolation_group_id: str | None = Field(None, alias="isolationGroupId")
    isolation_groups: list[IsolationGroup] | None = Field(None, alias="isolationGroups")
    use_cloud_gateway: bool | None = Field(None, alias="useCloudGateway")
    vpn_hubs: list[DeviceSettingsVpnHub] | None = Field(None, alias="vpnHubs")


class DeviceSettingsVpn(BaseModel):
    enabled: bool | None = None
    edge_to_data_center: bool | None = Field(None, alias="edgeToDataCenter")
    ref: Ref | None = None
    isolation_group_id: str | None = Field(None, alias="isolationGroupId")
    edge_to_edge_hub: EdgeToEdgeHub1 | None = Field(None, alias="edgeToEdgeHub")
    edge_to_edge: bool | None = Field(None, alias="edgeToEdge")
    edge_to_edge_detail: EdgeToEdgeDetail2 | None = Field(
        None, alias="edgeToEdgeDetail"
    )
    conditional_backhaul: bool | None = Field(None, alias="conditionalBackhaul")
    back_haul_edges: list[DeviceSettingsVpnHub] | None = Field(
        None, alias="backHaulEdges"
    )


class Protocol2(str, Enum):
    RFC6035 = "RFC6035"


class DeviceSettingsVqmCollector(BaseModel):
    address: str | None = None
    port: int | None = None


class DeviceSettingsVqm(BaseModel):
    enabled: bool | None = None
    override: bool | None = None
    protocol: Protocol2 | None = None
    collectors: list[DeviceSettingsVqmCollector] | None = None


class DeviceSettingsVrrpVirtualRouter(BaseModel):
    cidr_ip: str | None = Field(None, alias="cidrIp")
    interface: str | None = None
    interval: int | None = None
    preempt: bool | None = None
    preempt_delay: int | None = Field(None, alias="preemptDelay")
    priority: int | None = None
    subinterface_id: int | None = Field(None, alias="subinterfaceId")
    vlan_id: int | None = Field(None, alias="vlanId")
    vrid: int | None = None


class DeviceSettingsVrrp(BaseModel):
    enabled: bool | None = None
    data: list[DeviceSettingsVrrpVirtualRouter] | None = None


class MetdataType(str, Enum):
    REGULAR = "REGULAR"
    CDE = "CDE"
    PRIVATE = "PRIVATE"


class ConfigurationModuleSegmentMetadata(BaseModel):
    name: str | None = None
    segment_id: int | None = Field(None, alias="segmentId")
    segment_logical_id: str | None = Field(None, alias="segmentLogicalId")
    type: MetdataType | None = None


class DeviceSettingsSegment(BaseModel):
    authentication: DeviceSettingsAuthentication | None = None
    bgp: DeviceSettingsBgp | None = None
    css: DeviceSettingsCloudSecurity | None = None
    secure_access: DeviceSettingsSecureAccess | None = Field(None, alias="secureAccess")
    edge_direct: DeviceSettingsNvsFromEdge | None = Field(None, alias="edgeDirect")
    dns: DeviceSettingsDns | None = None
    hand_off_controllers: DeviceSettingsHandoffGateways | None = Field(
        None, alias="handOffControllers"
    )
    hand_off_gateways: DeviceSettingsHandoffGateways | None = Field(
        None, alias="handOffGateways"
    )
    hub_interconnect: DeviceSettingsHubInterconnect | None = Field(
        None, alias="hubInterconnect"
    )
    multi_source_qos: DeviceSettingsMultiSourceQos | None = Field(
        None, alias="multiSourceQos"
    )
    multicast: DeviceSettingsMulticast | None = None
    nat: DeviceSettingsNat | None = None
    netflow: DeviceSettingsNetflow | None = None
    ntp: DeviceSettingsNtp | None = None
    ospf: DeviceSettingsOspf | None = None
    routes: Routes1 | None = None
    segment: ConfigurationModuleSegmentMetadata | None = None
    snmp: DeviceSettingsSnmp | None = None
    syslog: DeviceSettingsSyslog | None = None
    vpn: DeviceSettingsVpn | None = None
    vqm: DeviceSettingsVqm | None = None
    vrrp: DeviceSettingsVrrp | None = None


class DeviceSettingsSoftwareUpdateWindow(BaseModel):
    day: int | None = None
    begin_hour: int | None = Field(None, alias="beginHour")
    end_hour: int | None = Field(None, alias="endHour")


class DeviceSettingsSoftwareUpdate(BaseModel):
    windowed: bool | None = None
    window: DeviceSettingsSoftwareUpdateWindow | None = None


class DeviceSettingsTacacs(BaseModel):
    ref: Ref | None = None
    source_interface: str | None = Field(None, alias="sourceInterface")


class Vendor3(str, Enum):
    PALO_ALTO = "PaloAlto"
    CHECK_POINT = "CheckPoint"
    FORTINET = "Fortinet"
    CENT_OS = "CentOS"


class Edge(LogicalidReference):
    ref: constr(regex=r"deviceSettings:vnfs:edge") | None = None


class License(LogicalidReference):
    ref: constr(regex=r"deviceSettings:securityVnf:license") | None = None


class Service(LogicalidReference):
    ref: constr(regex=r"deviceSettings:securityVnf:service") | None = None


class DeviceSettingsSecurityVnfVm(BaseModel):
    type: constr(regex=r"securityVnf") | None = None
    vendor: Vendor3 | None = None
    edge: Edge | None = None
    license: License | None = None
    service: Service | None = None
    uuid: str | None = None
    uuid_timestamp: datetime | None = Field(None, alias="uuidTimestamp")


class SecurityVnf(BaseModel):
    vms: list[DeviceSettingsSecurityVnfVm] | None = None


class DeviceSettingsVnfs(BaseModel):
    edge: Edge | None = None
    has_vnfs: bool | None = Field(None, alias="hasVnfs")
    security_vnf: SecurityVnf | None = Field(None, alias="securityVnf")


class Vendor2(str, Enum):
    ZSCALER = "zscaler"


class Provider3(BaseModel):
    ref: constr(regex=r"deviceSettings:zscaler:iaasSubscription") | None = None
    logical_id: str | None = Field(None, alias="logicalId")


class Mtgre(BaseModel):
    enabled: bool | None = None


class Location1(BaseModel):
    logical_id: str | None = Field(None, alias="logicalId")
    cloud: str | None = None


class DisplayTimeUnit(str, Enum):
    DAY = "DAY"
    HOUR = "HOUR"
    MINUTE = "MINUTE"


class SurrogateRefreshTimeUnit(str, Enum):
    DAY = "DAY"
    HOUR = "HOUR"
    MINUTE = "MINUTE"


class DeviceSettingsZscalerLocationGatewayOptions(BaseModel):
    xff_forward_enabled: bool | None = Field(None, alias="xffForwardEnabled")
    auth_required: bool | None = Field(None, alias="authRequired")
    aup_enabled: bool | None = Field(None, alias="aupEnabled")
    aup_block_internet_until_accepted: bool | None = Field(
        None, alias="aupBlockInternetUntilAccepted"
    )
    aup_force_ssl_inspection: bool | None = Field(None, alias="aupForceSslInspection")
    aup_timeout_in_days: float | None = Field(None, alias="aupTimeoutInDays")
    caution_enabled: bool | None = Field(None, alias="cautionEnabled")
    surrogate_ip: bool | None = Field(None, alias="surrogateIP")
    idle_time_in_minutes: float | None = Field(None, alias="idleTimeInMinutes")
    display_time_unit: DisplayTimeUnit | None = Field(None, alias="displayTimeUnit")
    surrogate_ip_enforced_for_known_browsers: bool | None = Field(
        None, alias="surrogateIPEnforcedForKnownBrowsers"
    )
    surrogate_refresh_time_in_minutes: float | None = Field(
        None, alias="surrogateRefreshTimeInMinutes"
    )
    surrogate_refresh_time_unit: SurrogateRefreshTimeUnit | None = Field(
        None, alias="surrogateRefreshTimeUnit"
    )
    dn_bandwidth: float | None = Field(None, alias="dnBandwidth")
    up_bandwidth: float | None = Field(None, alias="upBandwidth")
    ips_control: bool | None = Field(None, alias="ipsControl")
    ofw_enabled: bool | None = Field(None, alias="ofwEnabled")


class Location(BaseModel):
    name: str | None = "null"
    gw_properties: DeviceSettingsZscalerLocationGatewayOptions | None = Field(
        None, alias="gwProperties"
    )


class DeviceSettingsZscalerSublocations(BaseModel):
    internal_id: str | None = Field(None, alias="internalId")
    name: str | None = None
    other_sub_location: bool | None = Field(None, alias="otherSubLocation")
    rule_id: str | None = Field("", alias="ruleId")
    gw_properties: DeviceSettingsZscalerLocationGatewayOptions | None = Field(
        None, alias="gwProperties"
    )
    vlans: list[float] | None = None
    include_all_vlans: bool | None = Field(None, alias="includeAllVlans")
    include_all_lan_interfaces: bool | None = Field(
        None, alias="includeAllLanInterfaces"
    )
    lan_routed_interfaces: list[str] | None = Field(None, alias="lanRoutedInterfaces")
    ip_address_selection_manual: bool | None = Field(
        None, alias="ipAddressSelectionManual"
    )
    ip_addresses: list[str] | None = Field(None, alias="ipAddresses")


class Config1(BaseModel):
    override: bool | None = None
    enabled: bool | None = None
    vendor: Vendor2 | None = None
    cloud: Cloud | None = None
    provider: Provider3 | None = None
    location: Location | None = None
    sub_locations: list[DeviceSettingsZscalerSublocations] | None = Field(
        None, alias="subLocations"
    )
    mtgre: Mtgre | None = None


class MtgreSite(BaseModel):
    ref: constr(regex=r"deviceSettings:zscaler:mtgreSite") | None = None
    logical_id: str | None = Field(None, alias="logicalId")


class SubLocation(BaseModel):
    internal_id: str | None = Field(None, alias="internalId")
    logical_id: str | None = Field(None, alias="logicalId")
    cloud: str | None = None
    other_sub_location: bool | None = Field(None, alias="otherSubLocation")


class Deployment(BaseModel):
    location: Location1 | None = None
    mtgre_site: MtgreSite | None = Field(None, alias="mtgreSite")
    sub_locations: list[SubLocation] | None = Field(None, alias="subLocations")


class DeviceSettingsZscaler(BaseModel):
    config: Config1 | None = None
    deployment: Deployment | None = None


class DeviceSettingsAutoSimSwitchover(BaseModel):
    enabled: bool | None = None
    switchover_interval: float | None = Field(None, alias="switchoverInterval")


class DeviceSettingsCcFirewall(BaseModel):
    enabled: bool


class SegmentBasedDeviceSettingsData(BaseModel):
    bfd: DeviceSettingsBfd | None = None
    ha: DeviceSettingsHa
    lan: DeviceSettingsLan | None = None
    loopback_interfaces: DeviceSettingsLoopbackInterfaces | None = Field(
        None, alias="loopbackInterfaces"
    )
    models: dict[str, DeviceSettingsModel] | None = None
    multi_source_qos: DeviceSettingsMultiSourceQos | None = Field(
        None, alias="multiSourceQos"
    )
    ntp: DeviceSettingsNtp | None = None
    ntp_server: DeviceSettingsNtpAsServer | None = Field(None, alias="ntpServer")
    radio_settings: DeviceSettingsRadioSettings | None = Field(
        None, alias="radioSettings"
    )
    l2_settings: DeviceSettingsL2Settings | None = Field(None, alias="l2Settings")
    global_i_pv6_settings: DeviceSettingsGlobalIPv6Settings | None = Field(
        None, alias="globalIPv6Settings"
    )
    routed_interfaces: list[DeviceSettingsRoutedInterface] | None = Field(
        None, alias="routedInterfaces"
    )
    segments: list[DeviceSettingsSegment] | None = None
    snmp: DeviceSettingsSnmp | None = None
    software_update: DeviceSettingsSoftwareUpdate | None = Field(
        None, alias="softwareUpdate"
    )
    tacacs: DeviceSettingsTacacs | None = None
    vnfs: DeviceSettingsVnfs | None = None
    zscaler: DeviceSettingsZscaler | None = None
    auto_sim_switchover: DeviceSettingsAutoSimSwitchover | None = Field(
        None, alias="autoSimSwitchover"
    )
    cc_firewall: DeviceSettingsCcFirewall = Field(alias="ccFirewall")


class DeviceSettingsModel(BaseModel):
    lan: DeviceSettingsLan | None = None
    routed_interfaces: list[DeviceSettingsRoutedInterface] | None = Field(
        None, alias="routedInterfaces"
    )


class OverlayPreference(str, Enum):
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"
    I_PV4V6 = "IPv4v6"


class Type21(str, Enum):
    DHCP = "DHCP"
    STATIC = "STATIC"
    PPPOE = "PPPOE"


class Type22(str, Enum):
    STATIC = "STATIC"
    DHCP_STATEFUL = "DHCP_STATEFUL"
    DHCP_STATELESS = "DHCP_STATELESS"
    DHCP_PD = "DHCP_PD"


class DeviceSettingsRoutedInterfaceAddressing(BaseModel):
    type: Type21 | None = None
    cidr_prefix: int | None = Field(None, alias="cidrPrefix")
    cidr_ip: str | None = Field(None, alias="cidrIp")
    netmask: str | None = None
    gateway: str | None = None
    username: str | None = None
    password: str | None = None


class DeviceSettingsRoutedInterfaceAddressingV6(BaseModel):
    type: Type22 | None = None
    cidr_prefix: int | None = Field(None, alias="cidrPrefix")
    cidr_ip: str | None = Field(None, alias="cidrIp")
    gateway: str | None = None
    netmask: str | None = None
    ra_enabled: bool | None = Field(False, alias="raEnabled")
    interface_address: str | None = Field(None, alias="interfaceAddress")
    tag: str | None = None
    tag_logical_id: str | None = Field(None, alias="tagLogicalId")


class DefaultAction(str, Enum):
    ADVERTISE = "ADVERTISE"
    IGNORE = "IGNORE"
    LEARN = "LEARN"


class Action5(str, Enum):
    ADVERTISE = "ADVERTISE"
    IGNORE = "IGNORE"
    LEARN = "LEARN"


class Filter1(BaseModel):
    cidr_ip: str | None = Field(None, alias="cidrIp")
    cidr_prefix: str | None = Field(None, alias="cidrPrefix")
    action: Action5 | None = None


class DeviceSettingsRoutedInterfaceOspfFilter(BaseModel):
    default_action: DefaultAction | None = Field(None, alias="defaultAction")
    filters: list[Filter1] | None = None


class DeviceSettingsRoutedInterfaceOspf(BaseModel):
    area: str | None = None
    authentication: bool | None = None
    auth_id: int | None = Field(None, alias="authId")
    auth_passphrase: str | None = Field(None, alias="authPassphrase")
    cost: int | None = None
    dead_timer: int | None = Field(None, alias="deadTimer")
    mode: str | None = None
    enabled: bool | None = None
    enable_bfd: bool | None = Field(None, alias="enableBfd")
    exclusion_routes: list[dict[str, Any]] | None = Field(None, alias="exclusionRoutes")
    hello_timer: int | None = Field(None, alias="helloTimer")
    inbound_route_learning: DeviceSettingsRoutedInterfaceOspfFilter | None = Field(
        None, alias="inboundRouteLearning"
    )
    md5_authentication: bool | None = Field(None, alias="md5Authentication")
    mtu: int | None = Field(None, alias="MTU")
    outbound_route_advertisement: DeviceSettingsRoutedInterfaceOspfFilter | None = (
        Field(None, alias="outboundRouteAdvertisement")
    )
    passive: bool | None = None
    vlan_id: int | None = Field(None, alias="vlanId")


class ClientPrefixDelegation(BaseModel):
    enabled: bool | None = None
    tag: str | None = None
    tag_logical_id: str | None = Field(None, alias="tagLogicalId")


class DeviceSettingsRoutedInterfaceV6Detail(BaseModel):
    addressing: DeviceSettingsRoutedInterfaceAddressingV6 | None = None
    wan_overlay: WanOverlay | None = Field(None, alias="wanOverlay")
    rpf: Rpf | None = None
    trusted: bool | None = None
    nat_direct: bool | None = Field(None, alias="natDirect")
    dhcp_server: DeviceSettingsDhcpV6 | None = Field(None, alias="dhcpServer")
    router_advertisement_host_settings: (
        DeviceSettingsRouterAdvertisementHostSettings | None
    ) = Field(None, alias="routerAdvertisementHostSettings")
    ospf: DeviceSettingsRoutedInterfaceOspf | None = None
    client_prefix_delegation: ClientPrefixDelegation | None = Field(
        None, alias="clientPrefixDelegation"
    )


class Mode2(str, Enum):
    ADSL2 = "adsl2"
    VDSL2 = "vdsl2"


class DeviceSettingsRoutedInterfaceDslSettings(BaseModel):
    pass


class DslSettings(BaseModel):
    mode: Mode2 | None = None
    properties: DeviceSettingsRoutedInterfaceDslSettings | None = None


class DeviceSettingsRoutedInterfaceL2(BaseModel):
    autonegotiation: bool | None = None
    speed: str | None = None
    duplex: Duplex | None = None
    mtu: int | None = Field(None, alias="MTU")
    los_detection: bool | None = Field(None, alias="losDetection")
    probe_interval: ProbeInterval | None = Field(None, alias="probeInterval")


class Type19(str, Enum):
    IGMP_V2 = "IGMP_V2"


class Igmp1(BaseModel):
    enabled: bool | None = None
    type: Type19 | None = None


class Type20(str, Enum):
    PIM_SM = "PIM_SM"


class Pim1(BaseModel):
    enabled: bool | None = None
    type: Type20 | None = None


class Multicast1(BaseModel):
    igmp: Igmp1 | None = None
    igmp_host_query_interval_seconds: int | None = Field(
        None, alias="igmpHostQueryIntervalSeconds"
    )
    igmp_max_query_response: int | None = Field(None, alias="igmpMaxQueryResponse")
    pim: Pim1 | None = None
    pim_keep_alive_timer_seconds: int | None = Field(
        None, alias="pimKeepAliveTimerSeconds"
    )
    pim_prune_interval_seconds: int | None = Field(
        None, alias="pimPruneIntervalSeconds"
    )
    pim_hello_timer_seconds: int | None = Field(None, alias="pimHelloTimerSeconds")


class SubinterfaceType(str, Enum):
    SECONDARY_IP = "SECONDARY_IP"
    SUB_INTERFACE = "SUB_INTERFACE"


class SfpType(str, Enum):
    STANDARD = "standard"
    DSL = "dsl"
    GPON = "gpon"


class DeviceSettingsRoutedInterface(BaseModel):
    override: bool | None = None
    disabled: bool | None = None
    disable_v4: bool | None = Field(None, alias="disableV4")
    disable_v6: bool | None = Field(None, alias="disableV6")
    overlay_preference: OverlayPreference | None = Field(
        None, alias="overlayPreference"
    )
    addressing: DeviceSettingsRoutedInterfaceAddressing | None = None
    v6_detail: DeviceSettingsRoutedInterfaceV6Detail | None = Field(
        None, alias="v6Detail"
    )
    advertise: bool | None = None
    cellular: Cellular | None = None
    """
    Applicable only for CELL interfaces
    """
    dhcp_server: DeviceSettingsDhcp | None = Field(None, alias="dhcpServer")
    dsl_settings: DslSettings | None = Field(None, alias="dslSettings")
    encrypt_overlay: bool | None = Field(None, alias="encryptOverlay")
    l2: DeviceSettingsRoutedInterfaceL2 | None = None
    multicast: Multicast1 | None = None
    name: str | None = None
    nat_direct: bool | None = Field(None, alias="natDirect")
    ospf: DeviceSettingsRoutedInterfaceOspf | None = None
    ping_response: bool | None = Field(True, alias="pingResponse")
    dns_proxy: bool | None = Field(False, alias="dnsProxy")
    evdsl_modem_attached: bool | None = Field(False, alias="evdslModemAttached")
    radius_authentication: RadiusAuthentication | None = Field(
        None, alias="radiusAuthentication"
    )
    segment_id: int | None = Field(None, alias="segmentId")
    sfp_type: SfpType | None = Field(None, alias="sfpType")
    subinterfaces: list[DeviceSettingsSubinterface] | None = None
    rpf: Rpf | None = None
    trusted: bool | None = None
    underlay_accounting: bool | None = Field(True, alias="underlayAccounting")
    vlan_id: int | None = Field(None, alias="vlanId")
    wan_overlay: WanOverlay | None = Field(None, alias="wanOverlay")


class DeviceSettingsSubinterface(DeviceSettingsRoutedInterface):
    subinterface_id: int | None = Field(None, alias="subinterfaceId")
    subinterface_type: SubinterfaceType | None = Field(None, alias="subinterfaceType")


SegmentBasedDeviceSettingsData.update_forward_refs()
DeviceSettingsModel.update_forward_refs()
