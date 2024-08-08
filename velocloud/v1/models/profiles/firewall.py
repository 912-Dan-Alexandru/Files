"""
Velocloud profile firewall settings section
"""
# pylint: disable=missing-docstring
# pylint: disable=line-too-long
from __future__ import annotations
from enum import Enum

from pydantic import BaseModel, Field


class MetdataType(str, Enum):
    REGULAR = "REGULAR"
    CDE = "CDE"
    PRIVATE = "PRIVATE"


class ConfigurationModuleSegmentMetadata(BaseModel):
    name: str | None = None
    segment_id: int | None = Field(None, alias="segmentId")
    segment_logical_id: str | None = Field(None, alias="segmentLogicalId")
    type: MetdataType | None = None


class FirewallSegment(BaseModel):
    firewall_logging_enabled: bool
    stateful_firewall_enabled: bool | None = None
    outbound: list[FirewallOutboundRule]
    segment: ConfigurationModuleSegmentMetadata


class FirewallSshKeys(BaseModel):
    key: str
    expiration: str
    username: str
    access_level: AccessLevel = Field(..., alias="accessLevel")


class StatefulFirewallSettings(BaseModel):
    established_tcp_flow_timeout: int | None = Field(
        None, alias="establishedTcpFlowTimeout"
    )
    non_established_tcp_flow_timeout: int | None = Field(
        None, alias="nonEstablishedTcpFlowTimeout"
    )
    udp_flow_timeout: int | None = Field(None, alias="udpFlowTimeout")
    other_flow_timeout: int | None = Field(None, alias="otherFlowTimeout")


class StatefulFirewallSettingsV6(BaseModel):
    established_tcp_flow_timeout: int | None = Field(
        None, alias="establishedTcpFlowTimeout"
    )
    non_established_tcp_flow_timeout: int | None = Field(
        None, alias="nonEstablishedTcpFlowTimeout"
    )
    udp_flow_timeout: int | None = Field(None, alias="udpFlowTimeout")
    other_flow_timeout: int | None = Field(None, alias="otherFlowTimeout")


class TcpBasedAttacks(BaseModel):
    invalid_flags: bool | None = Field(None, alias="invalidFlags")
    enable_land: bool | None = Field(None, alias="enableLand")
    enable_syn_fragment: bool | None = Field(None, alias="enableSynFragment")


class IcmpBasedAttacks(BaseModel):
    enable_ping_of_death: bool | None = Field(None, alias="enablePingOfDeath")
    enable_fragment: bool | None = Field(None, alias="enableFragment")


class IpBasedAttacks(BaseModel):
    enable_unknown_protocol: bool | None = Field(None, alias="enableUnknownProtocol")
    enable_insecure_options: bool | None = Field(None, alias="enableInsecureOptions")


class NetworkProtectionSettings(BaseModel):
    denylist_duration: int | None = Field(None, alias="denylistDuration")
    new_connection_threshold: int | None = Field(None, alias="newConnectionThreshold")
    denylist: bool | None = None
    detection_time: int | None = Field(None, alias="detectionTime")
    tcp_half_open_threshold_enabled: bool | None = Field(
        None, alias="tcpHalfOpenThresholdEnabled"
    )
    tcp_half_open_threshold: int | None = Field(None, alias="tcpHalfOpenThreshold")
    tcp_based_attacks_enabled: bool | None = Field(None, alias="tcpBasedAttacksEnabled")
    tcp_based_attacks: TcpBasedAttacks | None = Field(None, alias="tcpBasedAttacks")
    icmp_based_attacks_enabled: bool | None = Field(
        None, alias="icmpBasedAttacksEnabled"
    )
    icmp_based_attacks: IcmpBasedAttacks | None = Field(None, alias="icmpBasedAttacks")
    ip_based_attacks_enabled: bool | None = Field(None, alias="ipBasedAttacksEnabled")
    ip_based_attacks: IpBasedAttacks | None = Field(None, alias="ipBasedAttacks")


class Post(BaseModel):
    enabled: bool


class Ssh(BaseModel):
    enabled: bool
    allow_selected_ip: list[str] | None = Field(None, alias="allowSelectedIp")
    rule_logical_id: str | None = Field(None, alias="ruleLogicalId")


class LocalUi(BaseModel):
    enabled: bool
    allow_selected_ip: list[str] | None = Field(None, alias="allowSelectedIp")
    """
    List of IP addresses allowed UI access
    """
    port_number: int = Field(..., alias="portNumber")
    rule_logical_id: str | None = Field(None, alias="ruleLogicalId")


class Console(BaseModel):
    enabled: bool


class Snmp(BaseModel):
    enabled: bool
    allow_selected_ip: list[str] | None = Field(None, alias="allowSelectedIp")
    """
    List of IP addresses allowed SNMP access
    """
    rule_logical_id: str | None = Field(None, alias="ruleLogicalId")


class Icmp(BaseModel):
    enabled: bool
    allow_selected_ip: list[str] | None = Field(None, alias="allowSelectedIp")
    """
    List of IP addresses allowed ICMP access
    """
    rule_logical_id: str | None = Field(None, alias="ruleLogicalId")


class Services(BaseModel):
    logging_enabled: bool = Field(..., alias="loggingEnabled")
    post: Post | None = None
    ssh: Ssh | None = None
    local_ui: LocalUi | None = Field(None, alias="localUi")
    console: Console | None = None
    usb_disabled: bool | None = Field(None, alias="usb.disabled")
    snmp: Snmp | None = None
    icmp: Icmp | None = None


class AccessLevel(str, Enum):
    BASIC = "BASIC"
    PRIVILEGED = "PRIVILEGED"


class Type5(str, Enum):
    PORT_FORWARDING = "port_forwarding"
    ONE_TO_ONE_NAT = "one_to_one_nat"


class Nat(BaseModel):
    lan_ip: str
    lan_port: int | None = None
    outbound: bool | None = None


class Action(BaseModel):
    type: Type5
    nat: Nat
    interface: str
    """
    The name of the interface from which traffic should be forwarded
    """
    subinterface_id: int | None = Field(None, alias="subinterfaceId")


class AllowOrDeny(str, Enum):
    ALLOW = "allow"
    DENY = "deny"
    DROP = "drop"
    REJECT = "reject"
    SKIP = "skip"


class Action1(BaseModel):
    allow_or_deny: AllowOrDeny | None = None


class AllowOrDeny1(str, Enum):
    ALLOW = "allow"
    DENY = "deny"


class Action2(BaseModel):
    allow_or_deny: AllowOrDeny1


class SRuleType(str, Enum):
    EXACT = "exact"
    PREFIX = "prefix"
    WILDCARD = "wildcard"
    NETMASK = "netmask"


class DRuleType(str, Enum):
    EXACT = "exact"
    PREFIX = "prefix"
    WILDCARD = "wildcard"
    NETMASK = "netmask"


class IpVersion(str, Enum):
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"
    I_PV4V6 = "IPv4v6"


class FirewallRuleMatch(BaseModel):
    appid: int | None = Field(
        None,
        description="Integer ID corresponding to an application in the network-level"
        " application map",
    )
    classid: int | None = Field(
        None,
        description="Integer ID corresponding to an application class in the "
        "network-level application map",
    )
    dscp: int | None = Field(
        None,
        description="Integer ID indicating DSCP classification, where mappings are"
        " as follows: [EF:46,VA:44,AF11:10,AF12:12,AF13:14,AF21:18,AF22:20,AF23:22,"
        "AF31:26,AF32:28,AF33:30,AF41:34,AF42:36,AF43:38,CS0:0,CS1:8,CS2:16,CS3:24,"
        "CS4:32,CS5:40,CS6:48,CS7:56]",
    )
    ip_version: IpVersion | None = Field(
        None, alias="ipVersion", description="Ip Version /Addressing Version"
    )
    sip: str | None = Field(None, description="Source IP address")
    sip_v6: str | None = Field(None, alias="sipV6", description="Source IPv6 address")
    sport_high: int | None = Field(
        None, description="Upper bound of a source port range"
    )

    sport_low: int | None = Field(
        None, description="Lower bound of a source port range"
    )
    s_address_group: str | None = Field(
        None, alias="sAddressGroup", description="Source address group reference"
    )
    s_port_group: str | None = Field(
        None, alias="sPortGroup", description="Source port group reference"
    )
    ssm: str | None = Field(None, description="Source subnet mask, e.g. 255.255.255.0")

    smac: str | None = Field(None, description="Source MAC address")
    svlan: int | None = Field(None, description="Integer ID for the source VLAN")
    s_interface: str | None = Field(None, alias="sInterface")
    os_version: int | None = Field(
        None,
        description="Index corresponding to the OS in the array:"
        " [OTHER,WINDOWS,LINUX,MACOS,IOS,ANDROID,EDGE]",
    )
    hostname: str | None = None
    dip: str | None = Field(None, description="Destination IP address")
    dip_v6: str | None = Field(
        None, alias="dipV6", description="Destination IPv6 address"
    )
    dport_low: int | None = Field(
        None, description="Lower bound of a destination port range"
    )
    dport_high: int | None = Field(
        None, description="Upper bound of a destination port range"
    )
    d_address_group: str | None = Field(
        None, alias="dAddressGroup", description="Destination address group reference"
    )
    d_port_group: str | None = Field(
        None, alias="dPortGroup", description="Destination port group reference"
    )
    dsm: str | None = Field(
        None, description="Destination subnet mask e.g. 255.255.255.0"
    )
    dmac: str | None = Field(None, description="Destination MAC address")
    dvlan: int | None = Field(None, description="Integer ID for the destination VLAN")
    d_interface: str | None = Field(None, alias="dInterface")
    proto: int | None = Field(
        None, description="Integer ID corresponding to a protocol"
    )
    s_rule_type: SRuleType | None = Field(None, description="    Source rule type")
    d_rule_type: DRuleType | None = Field(None, description="Destination rule type")


class FirewallInboundRule(BaseModel):
    name: str | None = None
    match: FirewallRuleMatch
    action: Action
    rule_logical_id: str | None = Field(None, alias="ruleLogicalId")


class FirewallOutboundRule(BaseModel):
    name: str | None = None
    match: FirewallRuleMatch
    action: Action1
    rule_logical_id: str | None = Field(None, alias="ruleLogicalId")


class FirewallData(BaseModel):
    firewall_enabled: bool
    inbound_logging_enabled: bool | None = Field(None, alias="inboundLoggingEnabled")
    stateful_firewall_enabled: bool
    firewall_logging_enabled: bool
    syslog_forwarding: bool
    inbound: list[FirewallInboundRule]
    inbound_v6: list[FirewallInboundRule] = Field(alias="inboundV6")
    stateful_firewall_settings: StatefulFirewallSettings = Field(
        alias="statefulFirewallSettings"
    )
    stateful_firewall_settings_v6: StatefulFirewallSettingsV6 = Field(
        alias="statefulFirewallSettingsV6"
    )
    network_protection_settings: NetworkProtectionSettings = Field(
        alias="networkProtectionSettings"
    )
    network_protection_settings_v6: NetworkProtectionSettings = Field(
        alias="networkProtectionSettingsV6"
    )
    segments: list[FirewallSegment]
    services: Services
    ssh_keys: list[FirewallSshKeys] | None = Field(None, alias="sshKeys")


FirewallSegment.update_forward_refs()
