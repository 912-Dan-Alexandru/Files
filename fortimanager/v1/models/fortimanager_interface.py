"""
FortiManager Interface V1 Pydantic models
"""
# pylint: disable=line-too-long, too-many-lines
from enum import Enum

from pydantic import BaseModel, Field


class ClientOptionTypeEnum(str, Enum):
    """
    Enumeration for Client option types.
    """

    HEX = "hex"  # 0
    STRING = "string"  # 1
    IP = "ip"  # 2
    FQDN = "fqdn"  # 3


class Dhcp6ClientOptionsEnum(str, Enum):
    """
    Enumeration for Dhcp6 Client Options.
    """

    RAPID = "rapid"  # 1
    IAPD = "iapd"  # 2
    IANA = "iana"  # 4


class Dhcp6RelayTypeEnum(str, Enum):
    """
    Enumeration for Dhcp6 Relay Type.
    """

    REGULAR = "regular"  # 1


class Ip6AllowaccessEnum(str, Enum):
    """
    Enumeration for Ip6 Allow access.
    """

    HTTPS = "https"  # 1
    PING = "ping"  # 2
    SSH = "ssh"  # 4
    SNMP = "snmp"  # 8
    HTTP = "http"  # 16
    TELNET = "telnet"  # 32
    FGFM = "fgfm"  # 128
    FABRIC = "fabric"  # 16384


class Ip6ModeEnum(str, Enum):
    """
    Enumeration for Ip6 Mode.
    """

    STATIC = "static"  # 0
    DHCP = "dhcp"  # 1
    PPPOE = "pppoe"  # 2
    DELEGATED = "delegated"  # 6


class Ip6PrefixModeEnum(str, Enum):
    """
    Enumeration for Ip6 Prefix Mode.
    """

    DHCP6 = "dhcp6"  # 1
    RA = "ra"  # 2


class NdModeEnum(str, Enum):
    """
    Enumeration for Nd Mode.
    """

    BASIC = "basic"  # 0
    SEND_COMPATIBLE = "SEND-compatible"  # 1


class AuthTypeEnum(str, Enum):
    """
    Enumeration for Auth Type.
    """

    AUTO = "auto"  # 4
    PAP = "pap"  # 8
    CHAP = "chap"  # 16
    MSCHAPV1 = "mschapv1"  # 32
    MSCHAPV2 = "mschapv2"  # 64


class AllowaccessEnum(str, Enum):
    """
    Enumeration for Allow access.
    """

    HTTPS = "https"  # 1
    PING = "ping"  # 2
    SSH = "ssh"  # 4
    SNMP = "snmp"  # 8
    HTTP = "http"  # 16
    TELNET = "telnet"  # 32
    FGFM = "fgfm"  # 128
    RADIUS_ACCT = "radius-acct"  # 512
    PROBE_RESPONSE = "probe-response"  # 1024
    FTM = "ftm"  # 8192
    FABRIC = "fabric"  # 16384
    SPEED_TEST = "speed-test"  # 32768


class StatusEnum(str, Enum):
    """
    Enumeration for Status.
    """

    DISABLE = "disable"  # 0
    ENABLE = "enable"  # 1


class VersionEnum(str, Enum):
    """
    Enumeration for Version.
    """

    V2 = "2"  # 2
    V3 = "3"  # 3


class AlgorithmEnum(str, Enum):
    """
    Enumeration for the Algorithm.
    """

    L2 = "L2"  # 0
    L3 = "L3"  # 1
    L4 = "L4"  # 2


class BfdEnum(str, Enum):
    """
    Enumeration for Bfd.
    """

    GLOBAL = "global"  # 0
    ENABLE = "enable"  # 1
    DISABLE = "disable"  # 2


class DedicatedToEnum(str, Enum):
    """
    Enumeration for Dedicated To.
    """

    NONE = "none"  # 0
    MANAGEMENT = "management"  # 1


class DhcpRelayInterfaceSelectMethodEnum(str, Enum):
    """
    Enumeration for Dhcp Relay Interface Select Method.
    """

    AUTO = "auto"  # 0
    SDWAN = "sdwan"  # 1
    SPECIFY = "specify"  # 2


class DhcpRelayTypeEnum(str, Enum):
    """
    Enumeration for Dhcp Relay Type.
    """

    REGULAR = "regular"  # 0
    IPSEC = "ipsec"  # 1


class DnsServerProtocolEnum(str, Enum):
    """
    Enumeration for Dns Server Protocol.
    """

    CLEARTEXT = "cleartext"  # 1
    DOT = "dot"  # 2
    DOH = "doh"  # 4


class FailActionOnExtenderEnum(str, Enum):
    """
    Enumeration for Fail Action On Extender.
    """

    SOFT_RESTART = "soft-restart"  # 0
    HARD_RESTART = "hard-restart"  # 1
    REBOOT = "reboot"  # 2


class FailAlertMethodEnum(str, Enum):
    """
    Enumeration for Fail Alert Method.
    """

    LINK_FAILED_SIGNAL = "link-failed-signal"  # 0
    LINK_DOWN = "link-down"  # 1


class FailDetectOptionEnum(str, Enum):
    """
    Enumeration for Fail Detect Option.
    """

    DETECTSERVER = "detectserver"  # 1
    LINK_DOWN = "link-down"  # 2


class FortilinkNeighborDetectEnum(str, Enum):
    """
    Enumeration for Fortilink Neighbor Detect.
    """

    LLDP = "lldp"  # 0
    FORTILINK = "fortilink"  # 1


class LacpModeEnum(str, Enum):
    """
    Enumeration for Lacp Mode.
    """

    STATIC = "static"  # 0
    PASSIVE = "passive"  # 1
    ACTIVE = "active"  # 2


class LacpSpeedEnum(str, Enum):
    """
    Enumeration for Lacp Speed.
    """

    SLOW = "slow"  # 0
    FAST = "fast"  # 1


class LldpReceptionEnum(str, Enum):
    """
    Enumeration for Lldp Reception.
    """

    DISABLE = "disable"  # 0
    ENABLE = "enable"  # 1
    VDOM = "vdom"  # 3


class LldpTransmissionEnum(str, Enum):
    """
    Enumeration for Lldp Transmission.
    """

    ENABLE = "enable"  # 0
    DISABLE = "disable"  # 1
    VDOM = "vdom"  # 2


class ManagedSubnetworkSizeEnum(str, Enum):
    """
    Enumeration for Managed Subnetwork Size.
    """

    S_32 = "32"  # 32
    S_64 = "64"  # 64
    S_128 = "128"  # 128
    S_256 = "256"  # 256
    S_512 = "512"  # 512
    S_1024 = "1024"  # 1024
    S_2048 = "2048"  # 2048
    S_4096 = "4096"  # 4096
    S_8192 = "8192"  # 8192
    S_16384 = "16384"  # 16384
    S_32768 = "32768"  # 32768
    S_65536 = "65536"  # 65536


class MinLinksDownEnum(str, Enum):
    """
    Enumeration for Min Links Down.
    """

    OPERATIONAL = "operational"  # 0
    ADMINISTRATIVE = "administrative"  # 1


class ModeEnum(str, Enum):
    """
    Enumeration for Mode.
    """

    STATIC = "static"  # 0
    DHCP = "dhcp"  # 1
    PPPOE = "pppoe"  # 2
    PPPOA = "pppoa"  # 3


class NetflowSamplerEnum(str, Enum):
    """
    Enumeration for Netflow Sampler.
    """

    DISABLE = "disable"  # 0
    TX = "tx"  # 1
    RX = "rx"  # 2
    BOTH = "both"  # 3


class PptpAuthTypeEnum(str, Enum):
    """
    Enumeration for Pptp Auth Type.
    """

    AUTO = "auto"  # 4
    PAP = "pap"  # 8
    CHAP = "chap"  # 16
    MSCHAPV1 = "mschapv1"  # 32
    MSCHAPV2 = "mschapv2"  # 64


class RoleEnum(str, Enum):
    """
    Enumeration for Role.
    """

    LAN = "lan"  # 0
    WAN = "wan"  # 1
    DMZ = "dmz"  # 2
    UNDEFINED = "undefined"  # 3


class SampleDirectionEnum(str, Enum):
    """
    Enumeration for Sample Direction.
    """

    RX = "rx"  # 1
    TX = "tx"  # 2
    BOTH = "both"  # 3


class Security8021xModeEnum(str, Enum):
    """
    Enumeration for Security 8021x Mode.
    """

    DEFAULT = "default"  # 0
    DYNAMIC_VLAN = "dynamic-vlan"  # 1
    FALLBACK = "fallback"  # 2
    SLAVE = "slave"  # 3


class SecurityMacAuthBypassEnum(str, Enum):
    """
    Enumeration for Security Mac Auth Bypass.
    """

    DISABLE = "disable"  # 0
    ENABLE = "enable"  # 1
    MAC_AUTH_ONLY = "mac-auth-only"  # 3


class SecurityModeEnum(str, Enum):
    """
    Enumeration for Security Mode.
    """

    NONE = "none"  # 1
    CAPTIVE_PORTAL = "captive-portal"  # 2
    MODE_802_1X = "802.1X"  # 3


class SpeedEnum(str, Enum):
    """
    Enumeration for Speed.
    """

    AUTO = "auto"  # 1
    SPEED_10FULL = "10full"  # 2
    SPEED_10HALF = "10half"  # 4
    SPEED_100FULL = "100full"  # 8
    SPEED_100HALF = "100half"  # 16
    SPEED_1000FULL = "1000full"  # 32
    SPEED_1000AUTO = "1000auto"  # 256


class InterfaceStatusEnum(str, Enum):
    """
    Enumeration for Interface Status.
    """

    DOWN = "down"  # 0
    UP = "up"  # 1


class StpHaSecondaryEnum(str, Enum):
    """
    Enumeration for StpHa Secondary.
    """

    DISABLE = "disable"  # 0
    ENABLE = "enable"  # 1
    PRIORITY_ADJUST = "priority-adjust"  # 2


class StpforwardModeEnum(str, Enum):
    """
    Enumeration for Stpforward Mode.
    """

    RPL_ALL_EXT_ID = "rpl-all-ext-id"  # 0
    RPL_BRIDGE_EXT_ID = "rpl-bridge-ext-id"  # 1
    RPL_NOTHING = "rpl-nothing"  # 2


class SwitchControllerFeatureEnum(str, Enum):
    """
    Enumeration for Switch Controller Feature.
    """

    NONE = "none"  # 0
    DEFAULT_VLAN = "default-vlan"  # 1
    QUARANTINE = "quarantine"  # 2
    VOICE = "voice"  # 4
    RSPAN = "rspan"  # 6
    VIDEO = "video"  # 7
    NAC = "nac"  # 8
    NAC_SEGMENT = "nac-segment"  # 9


class SwitchControllerSourceIpEnum(str, Enum):
    """
    Enumeration for Switch Controller Source Ip.
    """

    OUTBOUND = "outbound"  # 1
    FIXED = "fixed"  # 2


class SystemIdTypeEnum(str, Enum):
    """
    Enumeration for System Id Type.
    """

    AUTO = "auto"  # 1
    USER = "user"  # 2


class TypeEnum(str, Enum):
    """
    Enumeration for Type.
    """

    PHYSICAL = "physical"  # 0
    VLAN = "vlan"  # 1
    AGGREGATE = "aggregate"  # 2
    REDUNDANT = "redundant"  # 3
    TUNNEL = "tunnel"  # 4
    LOOPBACK = "loopback"  # 7
    VDOM_LINK = "vdom-link"  # 6
    SWITCH = "switch"  # 8
    HARD_SWITCH = "hard-switch"  # 9
    HDLC = "hdlc"  # 10
    VAP_SWITCH = "vap-switch"  # 11
    WL_MESH = "wl-mesh"  # 12
    SWITCH_VLAN = "switch-vlan"  # 14
    FEXT_WAN = "fext-wan"  # 17
    VXLAN = "vxlan"  # 18
    EMAC_VLAN = "emac-vlan"  # 19
    GENEVE = "geneve"  # 20
    SSL = "ssl"  # 21
    LAN_EXTENSION = "lan-extension"  # 22


class VlanProtocolEnum(str, Enum):
    """
    Enumeration for Vlan Protocol.
    """

    P_8021Q = "8021q"  # 0
    P_8021AD = "8021ad"  # 1


class ClientOptions(BaseModel):
    """
    DHCP client options model.
    """

    code: int = Field(default=0, description="DHCP client option code.", le=255)
    id: int = Field(default=0, description="ID.", le=4294967295)
    ip: list[str] = Field(..., description="DHCP option IPs.")
    type: TypeEnum = Field(
        default=ClientOptionTypeEnum.HEX, description="DHCP client option type."
    )
    value: str = Field(..., description="DHCP client option value.", max_length=312)


class DhcpSnoopingServerList(BaseModel):
    """
    Configure DHCP server access list.
    """

    name: str = Field(default="default", description="DHCP server name.", max_length=35)
    server_ip: str = Field(
        alias="server-ip", default="0.0.0.0", description="IP address for DHCP server."
    )


class Ipv6(BaseModel):
    """
    IPv6 of interface model.
    """

    autoconf: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable address auto config."
    )
    cli_conn6_status: int = Field(alias="cli-conn6-status", default=0, le=4294967295)
    dhcp6_client_options: Dhcp6ClientOptionsEnum = Field(
        ..., alias="dhcp6-client-options"
    )
    dhcp6_information_request: StatusEnum = Field(
        alias="dhcp6-information-request",
        default=StatusEnum.DISABLE,
        description="Enable/disable DHCPv6 information request.",
    )
    dhcp6_prefix_delegation: StatusEnum = Field(
        alias="dhcp6-prefix-delegation",
        default=StatusEnum.DISABLE,
        description="Enable/disable DHCPv6 prefix delegation.",
    )
    dhcp6_relay_ip: str = Field(
        ..., alias="dhcp6-relay-ip", description="DHCPv6 relay IP address."
    )
    dhcp6_relay_service: StatusEnum = Field(
        alias="dhcp6-relay-service",
        default=StatusEnum.DISABLE,
        description="Enable/disable DHCPv6 relay.",
    )
    dhcp6_relay_type: Dhcp6RelayTypeEnum = Field(
        alias="dhcp6-relay-type",
        default=Dhcp6RelayTypeEnum.REGULAR,
        description="DHCPv6 relay type.",
    )
    icmp6_send_redirect: StatusEnum = Field(
        alias="icmp6-send-redirect",
        default=StatusEnum.ENABLE,
        description="Enable/disable sending of ICMPv6 redirects.",
    )
    interface_identifier: str = Field(
        alias="interface-identifier",
        default="::",
        description="IPv6 interface identifier.",
    )
    ip6_address: str = Field(
        alias="ip6-address",
        default="::/0",
        description="Primary IPv6 address prefix. Syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx.",
    )
    ip6_allowaccess: Ip6AllowaccessEnum = Field(
        ...,
        alias="ip6-allowaccess",
        description="Allow management access to the interface.",
    )
    ip6_default_life: int = Field(
        alias="ip6-default-life",
        default=1800,
        description="Default life (sec).",
        le=9000,
    )
    ip6_delegated_prefix_iaid: int = Field(
        alias="ip6-delegated-prefix-iaid",
        default=0,
        description="IAID of obtained delegated-prefix from the upstream interface.",
        le=4294967295,
    )
    ip6_dns_server_override: StatusEnum = Field(
        alias="ip6-dns-server-override",
        default=StatusEnum.ENABLE,
        description="Enable/disable using the DNS server acquired by DHCP.",
    )
    ip6_hop_limit: int = Field(
        alias="ip6-hop-limit",
        default=0,
        description="Hop limit (0 means unspecified).",
        le=255,
    )
    ip6_link_mtu: int = Field(
        alias="ip6-link-mtu",
        default=0,
        description="IPv6 link MTU.",
        le=16000,
        ge=1280,
    )
    ip6_manage_flag: StatusEnum = Field(
        alias="ip6-manage-flag",
        default=StatusEnum.DISABLE,
        description="Enable/disable the managed flag.",
    )
    ip6_max_interval: int = Field(
        alias="ip6-max-interval",
        default=600,
        description="IPv6 maximum interval (4 to 1800 sec).",
        le=1800,
        ge=4,
    )
    ip6_min_interval: int = Field(
        alias="ip6-min-interval",
        default=198,
        description="IPv6 minimum interval (3 to 1350 sec).",
        le=1350,
        ge=3,
    )
    ip6_mode: Ip6ModeEnum = Field(
        alias="ip6-mode",
        default=Ip6ModeEnum.STATIC,
        description="Addressing mode (static, DHCP, delegated).",
    )
    ip6_other_flag: StatusEnum = Field(
        alias="ip6-other-flag",
        default=StatusEnum.DISABLE,
        description="Enable/disable the other IPv6 flag.",
    )
    ip6_prefix_mode: Ip6PrefixModeEnum = Field(
        alias="ip6-prefix-mode",
        default=Ip6PrefixModeEnum.DHCP6,
        description="Assigning a prefix from DHCP or RA.",
    )
    ip6_reachable_time: int = Field(
        alias="ip6-reachable-time",
        default=0,
        description="IPv6 reachable time (milliseconds; 0 means unspecified).",
        le=3600000,
    )
    ip6_retrans_time: int = Field(
        alias="ip6-retrans-time",
        default=0,
        description="IPv6 retransmit time (milliseconds; 0 means unspecified).",
        le=4294967295,
    )
    ip6_send_adv: StatusEnum = Field(
        alias="ip6-send-adv",
        default=StatusEnum.DISABLE,
        description="Enable/disable sending advertisements about the interface.",
    )
    ip6_subnet: str = Field(
        alias="ip6-subnet",
        default="::/0",
        description="Subnet to routing prefix. Syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx.",
    )
    ip6_upstream_interface: str | list = Field(
        ...,
        alias="ip6-upstream-interface",
        description="Interface name providing delegated information.",
    )
    nd_cert: str | list = Field(
        ..., alias="nd-cert", description="Neighbor discovery certificate."
    )
    nd_cga_modifier: str = Field(
        alias="nd-cga-modifier",
        default="00000000000000002573282564293A20",
        description="Neighbor discovery CGA modifier.",
    )
    nd_mode: NdModeEnum = Field(
        alias="nd-mode",
        default=NdModeEnum.BASIC,
        description="Neighbor discovery mode.",
    )
    nd_security_level: int = Field(
        alias="nd-security-level",
        default=0,
        description="Neighbor discovery security level (0 - 7; 0 = least secure, default = 0).",
        le=7,
    )
    nd_timestamp_delta: int = Field(
        alias="nd-timestamp-delta",
        default=300,
        description="Neighbor discovery timestamp delta value (1 - 3600 sec; default = 300).",
        le=3600,
        ge=1,
    )
    nd_timestamp_fuzz: int = Field(
        alias="nd-timestamp-fuzz",
        default=1,
        description="Neighbor discovery timestamp fuzz factor (1 - 60 sec; default = 1).",
        le=60,
        ge=1,
    )
    ra_send_mtu: StatusEnum = Field(
        alias="ra-send-mtu",
        default=StatusEnum.ENABLE,
        description="Enable/disable sending link MTU in RA packet.",
    )
    unique_autoconf_addr: StatusEnum = Field(
        alias="unique-autoconf-addr",
        default=StatusEnum.DISABLE,
        description="Enable/disable unique auto config address.",
    )
    vrip6_link_local: str = Field(
        default="::", description="Link-local IPv6 address of virtual router."
    )
    vrrp_virtual_mac6: StatusEnum = Field(
        alias="vrrp-virtual-mac6",
        default=StatusEnum.DISABLE,
        description="Enable/disable virtual MAC for VRRP.",
    )


class L2tpClientSettings(BaseModel):
    """
    L2TP client settings.
    """

    auth_type: AuthTypeEnum = Field(
        alias="auth-type",
        default=AuthTypeEnum.AUTO,
        description="L2TP authentication type.",
    )
    defaultgw: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable default gateway."
    )
    distance: int = Field(
        default=2, description="Distance of learned routes.", le=255, ge=1
    )
    hello_interval: int = Field(
        alias="hello-interval",
        default=60,
        description="L2TP hello message interval in seconds (0 - 3600 sec, default = 60).",
        le=3600,
    )
    ip: str = Field(default="0.0.0.0 0.0.0.0")
    mtu: int = Field(default=1460, description="L2TP MTU.", le=65535, ge=40)
    password: str = Field(
        default="ENC 5tooehwbC1hLzc8nxg3Ocwq9r4L7ilxHvQwi2tHm9fC2S2/1z5KZSRirppTRvji+d639dm7S2Fc52K1NRsAqOc3Z1tMzKVVuVA0Uw/b7zSFtmijR8lVvBTVlEw/cj3qIPzGlM2MHhv05W+fheDRjJ1c3SE/pkLDPi0FmjG8FPes5FQXfUss+CH+btm44HgE+2/RM1w==",
        description="L2TP password.",
    )
    peer_host: str = Field(
        ..., alias="peer-host", description="L2TP peer host address.", max_length=255
    )
    peer_mask: str = Field(
        alias="peer-mask", default="255.255.255.255", description="L2TP peer mask."
    )
    peer_port: int = Field(
        alias="peer-port",
        default=1701,
        description="L2TP peer port number.",
        le=65535,
        ge=1,
    )
    priority: int = Field(
        default=1, description="Priority of learned routes.", le=65535, ge=1
    )
    user: str = Field(..., description="L2TP user name.", max_length=127)


class Secondaryip(BaseModel):
    """
    Second IP address of interface.
    """

    allowaccess: AllowaccessEnum = Field(
        ..., description="Management access settings for the secondary IP address."
    )
    id: int = Field(default=0, description="ID.", le=4294967295)
    ip: str = Field(
        default="0.0.0.0 0.0.0.0", description="Secondary IP address of the interface."
    )


class Tagging(BaseModel):
    """
    Config object tagging.
    """

    category: str = Field(..., description="Tag category.")
    name: str = Field(..., description="Tagging entry name.", max_length=63)
    tags: list[str] = Field(..., description="Tags.")


class Vrrp(BaseModel):
    """
    VRRP configuration model.
    """

    accept_mode: StatusEnum = Field(
        alias="accept-mode",
        default=StatusEnum.ENABLE,
        description="Enable/disable accept mode.",
    )
    adv_interval: int = Field(
        alias="adv-interval",
        default=1,
        description="Advertisement interval (1 - 255 seconds).",
        le=255,
        ge=1,
    )
    ignore_default_route: StatusEnum = Field(
        alias="ignore-default-route",
        default=StatusEnum.DISABLE,
        description="Enable/disable ignoring of default route when checking destination.",
    )
    preempt: StatusEnum = Field(
        default=StatusEnum.ENABLE, description="Enable/disable preempt mode."
    )
    priority: int = Field(
        default=100,
        description="Priority of the virtual router (1 - 255).",
        le=255,
        ge=1,
    )
    start_time: int = Field(
        alias="start-time",
        default=3,
        description="Startup time (1 - 255 seconds).",
        le=255,
        ge=1,
    )
    status: StatusEnum = Field(
        default=StatusEnum.ENABLE, description="Enable/disable this VRRP configuration."
    )
    version: VersionEnum = Field(default=VersionEnum.V2, description="VRRP version.")
    vrdst: list[str] = Field(..., description="Monitor the route to this destination.")
    vrdst_priority: int = Field(
        alias="vrdst-priority",
        default=0,
        description="Priority of the virtual router when the virtual router destination becomes unreachable (0 - 254).",
        le=254,
    )
    vrgrp: int = Field(
        default=0, description="VRRP group ID (1 - 65535).", le=65535, ge=1
    )
    vrid: int = Field(
        default=0, description="Virtual router identifier (1 - 255).", le=255, ge=1
    )
    vrip: str = Field(
        default="0.0.0.0", description="IP address of the virtual router."
    )


class SystemInterface(BaseModel, allow_population_by_field_name=True):
    """
    System Interface model.
    """

    ac_name: str | None = Field(
        default=None, alias="ac-name", description="PPPoE server name.", max_length=63
    )
    aggregate: str | None = Field(default=None, max_length=15)
    algorithm: AlgorithmEnum = Field(
        default=AlgorithmEnum.L4, description="Frame distribution algorithm."
    )
    alias: str | None = Field(
        default=None,
        description="Alias will be displayed with the interface name to make it easier to distinguish.",
        max_length=25,
    )
    allowaccess: AllowaccessEnum | None = Field(
        default=None,
        description="Permitted types of management access to this interface.",
    )
    ap_discover: StatusEnum = Field(
        alias="ap-discover",
        default=StatusEnum.ENABLE,
        description="Enable/disable automatic registration of unknown FortiAP devices.",
    )
    arpforward: StatusEnum = Field(
        default=StatusEnum.ENABLE, description="Enable/disable ARP forwarding."
    )
    auth_cert: str | None | list = Field(
        default=None, alias="auth-cert", description="HTTPS server certificate."
    )
    auth_portal_addr: str | None = Field(
        default=None,
        alias="auth-portal-addr",
        description="Address of captive portal.",
        max_length=63,
    )
    auth_type: AuthTypeEnum = Field(
        alias="auth-type",
        default=AuthTypeEnum.AUTO,
        description="PPP authentication type to use.",
    )
    auto_auth_extension_device: StatusEnum = Field(
        alias="auto-auth-extension-device",
        default=StatusEnum.DISABLE,
        description="Enable/disable automatic authorization of dedicated Fortinet extension device on this interface.",
    )
    bandwidth_measure_time: int = Field(
        alias="bandwidth-measure-time",
        default=0,
        description="Bandwidth measure time.",
        le=4294967295,
    )
    bfd: BfdEnum = Field(
        default=BfdEnum.GLOBAL,
        description="Bidirectional Forwarding Detection (BFD) settings.",
    )
    bfd_desired_min_tx: int = Field(
        alias="bfd-desired-min-tx",
        default=250,
        description="BFD desired minimal transmit interval.",
        le=100000,
        ge=1,
    )
    bfd_detect_mult: int = Field(
        alias="bfd-detect-mult",
        default=3,
        description="BFD detection multiplier.",
        le=50,
        ge=1,
    )
    bfd_required_min_rx: int = Field(
        alias="bfd-required-min-rx",
        default=250,
        description="BFD required minimal receive interval.",
        le=100000,
        ge=1,
    )
    broadcast_forward: StatusEnum = Field(
        alias="broadcast-forward",
        default=StatusEnum.DISABLE,
        description="Enable/disable broadcast forwarding.",
    )
    captive_portal: int = Field(
        alias="captive-portal",
        default=0,
        description="Enable/disable captive portal.",
        le=4294967295,
    )
    cli_conn_status: int = Field(alias="cli-conn-status", default=0, le=4294967295)
    color: int = Field(default=0, description="Color of icon on the GUI.", le=32)
    dedicated_to: DedicatedToEnum = Field(
        alias="dedicated-to",
        default=DedicatedToEnum.NONE,
        description="Configure interface for single purpose.",
    )
    defaultgw: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        description="Enable to get the gateway IP from the DHCP or PPPoE server.",
    )
    description: str | None = Field(
        default=None, description="Description.", max_length=255
    )
    detected_peer_mtu: int = Field(alias="detected-peer-mtu", default=0, le=4294967295)
    device_identification: StatusEnum = Field(
        alias="device-identification",
        default=StatusEnum.DISABLE,
        description="Enable/disable passively gathering of device identity information about the devices on the network connected to this interface.",
    )
    device_user_identification: StatusEnum = Field(
        alias="device-user-identification",
        default=StatusEnum.ENABLE,
        description="Enable/disable passive gathering of user identity information about users on this interface.",
    )
    devindex: int = Field(default=0, le=4294967295)
    dhcp_classless_route_addition: StatusEnum = Field(
        alias="dhcp-classless-route-addition",
        default=StatusEnum.DISABLE,
        description="Enable/disable addition of classless static routes retrieved from DHCP server.",
    )
    dhcp_client_identifier: str | None = Field(
        default=None,
        alias="dhcp-client-identifier",
        description="DHCP client identifier.",
        max_length=48,
    )
    dhcp_relay_agent_option: StatusEnum = Field(
        alias="dhcp-relay-agent-option",
        default=StatusEnum.ENABLE,
        description="Enable/disable DHCP relay agent option.",
    )
    dhcp_relay_interface: str | list | None = Field(
        default=None,
        alias="dhcp-relay-interface",
        description="Specify outgoing interface to reach server.",
    )
    dhcp_relay_interface_select_method: DhcpRelayInterfaceSelectMethodEnum = Field(
        alias="dhcp-relay-interface-select-method",
        default=DhcpRelayInterfaceSelectMethodEnum.AUTO,
        description="Specify how to select outgoing interface to reach server.",
    )
    dhcp_relay_ip: list[str] | None = Field(
        default=None, alias="dhcp-relay-ip", description="DHCP relay IP address."
    )
    dhcp_relay_link_selection: str = Field(
        alias="dhcp-relay-link-selection",
        default="0.0.0.0",
        description="DHCP relay link selection.",
    )
    dhcp_relay_request_all_server: StatusEnum = Field(
        alias="dhcp-relay-request-all-server",
        default=StatusEnum.DISABLE,
        description="Enable/disable sending of DHCP requests to all servers.",
    )
    dhcp_relay_service: StatusEnum = Field(
        alias="dhcp-relay-service",
        default=StatusEnum.DISABLE,
        description="Enable/disable allowing this interface to act as a DHCP relay.",
    )
    dhcp_relay_type: DhcpRelayTypeEnum = Field(
        alias="dhcp-relay-type",
        default=DhcpRelayTypeEnum.REGULAR,
        description="DHCP relay type (regular or IPsec).",
    )
    dhcp_renew_time: int = Field(
        alias="dhcp-renew-time",
        default=0,
        description="DHCP renew time in seconds (300-604800), 0 means use the renew time provided by the server.",
        le=604800,
        ge=300,
    )
    disc_retry_timeout: int = Field(
        alias="disc-retry-timeout",
        default=1,
        description="Time in seconds to wait before retrying to start a PPPoE discovery, 0 means no timeout.",
        le=4294967295,
    )
    disconnect_threshold: int = Field(
        alias="disconnect-threshold",
        default=0,
        description="Time in milliseconds to wait before sending a notification that this interface is down or disconnected.",
        le=10000,
    )
    distance: int = Field(
        default=5,
        description="Distance for routes learned through PPPoE or DHCP, lower distance indicates preferred route.",
        le=255,
        ge=1,
    )
    dns_server_override: StatusEnum = Field(
        alias="dns-server-override",
        default=StatusEnum.ENABLE,
        description="Enable/disable use DNS acquired by DHCP or PPPoE.",
    )
    dns_server_protocol: DnsServerProtocolEnum = Field(
        alias="dns-server-protocol",
        default=DnsServerProtocolEnum.CLEARTEXT,
        description="DNS transport protocols.",
    )
    drop_fragment: StatusEnum = Field(
        alias="drop-fragment",
        default=StatusEnum.DISABLE,
        description="Enable/disable drop fragment packets.",
    )
    drop_overlapped_fragment: StatusEnum = Field(
        alias="drop-overlapped-fragment",
        default=StatusEnum.DISABLE,
        description="Enable/disable drop overlapped fragment packets.",
    )
    egress_shaping_profile: str | list | None = Field(
        default=None,
        alias="egress-shaping-profile",
        description="Outgoing traffic shaping profile.",
    )
    estimated_downstream_bandwidth: int = Field(
        alias="estimated-downstream-bandwidth",
        default=0,
        description="Estimated maximum downstream bandwidth (kbps). Used to estimate link utilization.",
        le=4294967295,
    )
    estimated_upstream_bandwidth: int = Field(
        alias="estimated-upstream-bandwidth",
        default=0,
        description="Estimated maximum upstream bandwidth (kbps). Used to estimate link utilization.",
        le=4294967295,
    )
    explicit_ftp_proxy: StatusEnum = Field(
        alias="explicit-ftp-proxy",
        default=StatusEnum.DISABLE,
        description="Enable/disable the explicit FTP proxy on this interface.",
    )
    explicit_web_proxy: StatusEnum = Field(
        alias="explicit-web-proxy",
        default=StatusEnum.DISABLE,
        description="Enable/disable the explicit web proxy on this interface.",
    )
    external: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable/disable identifying the interface as an external interface (which usually means it's connected to the Internet).",
    )
    fail_action_on_extender: FailActionOnExtenderEnum = Field(
        alias="fail-action-on-extender",
        default=FailActionOnExtenderEnum.SOFT_RESTART,
        description="Action on FortiExtender when interface fail.",
    )
    fail_alert_interfaces: str | list | None = Field(
        default=None,
        alias="fail-alert-interfaces",
        description="Names of the FortiGate interfaces to which the link failure alert is sent.",
    )
    fail_alert_method: FailAlertMethodEnum = Field(
        alias="fail-alert-method",
        default=FailAlertMethodEnum.LINK_DOWN,
        description="Select link-failed-signal or link-down method to alert about a failed link.",
    )
    fail_detect: StatusEnum = Field(
        alias="fail-detect",
        default=StatusEnum.DISABLE,
        description="Enable/disable fail detection features for this interface.",
    )
    fail_detect_option: FailDetectOptionEnum = Field(
        alias="fail-detect-option",
        default=FailDetectOptionEnum.LINK_DOWN,
        description="Options for detecting that this interface has failed.",
    )
    fortilink: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable FortiLink to dedicate this interface to manage other Fortinet devices.",
    )
    fortilink_backup_link: int = Field(alias="fortilink-backup-link", default=0, le=255)
    fortilink_neighbor_detect: FortilinkNeighborDetectEnum = Field(
        alias="fortilink-neighbor-detect",
        default=FortilinkNeighborDetectEnum.FORTILINK,
        description="Protocol for FortiGate neighbor discovery.",
    )
    fortilink_split_interface: StatusEnum = Field(
        alias="fortilink-split-interface",
        default=StatusEnum.ENABLE,
        description="Enable/disable FortiLink split interface to connect member link to different FortiSwitch in stack for uplink redundancy.",
    )
    forward_domain: int = Field(
        alias="forward-domain",
        default=0,
        description="Transparent mode forward domain.",
        le=2147483647,
    )
    icmp_accept_redirect: StatusEnum = Field(
        alias="icmp-accept-redirect",
        default=StatusEnum.ENABLE,
        description="Enable/disable ICMP accept redirect.",
    )
    icmp_send_redirect: StatusEnum = Field(
        alias="icmp-send-redirect",
        default=StatusEnum.ENABLE,
        description="Enable/disable sending of ICMP redirects.",
    )
    ident_accept: StatusEnum = Field(
        alias="ident-accept",
        default=StatusEnum.DISABLE,
        description="Enable/disable authentication for this interface.",
    )
    idle_timeout: int = Field(
        alias="idle-timeout",
        default=0,
        description="PPPoE auto disconnect after idle timeout seconds, 0 means no timeout.",
        le=32767,
    )
    inbandwidth: int = Field(
        default=0,
        description="Bandwidth limit for incoming traffic (0 - 100000000 kbps), 0 means unlimited.",
        le=80000000,
    )
    ingress_shaping_profile: str | list | None = Field(
        default=None,
        alias="ingress-shaping-profile",
        description="Incoming traffic shaping profile.",
    )
    ingress_spillover_threshold: int = Field(
        alias="ingress-spillover-threshold",
        default=0,
        description="Ingress Spillover threshold (0 - 16776000 kbps), 0 means unlimited.",
        le=16776000,
    )
    interface: str | list = Field(..., description="Interface name.")
    internal: int = Field(default=0, description="Implicitly created.", le=255)
    ip: str = Field(
        default="0.0.0.0 0.0.0.0",
        description="Interface IPv4 address and subnet mask, syntax: X.X.X.X/24.",
    )
    ip_managed_by_fortiipam: StatusEnum = Field(
        alias="ip-managed-by-fortiipam",
        default=StatusEnum.DISABLE,
        description="Enable/disable automatic IP address assignment of this interface by FortiIPAM.",
    )
    ipmac: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable IP/MAC binding."
    )
    ips_sniffer_mode: StatusEnum = Field(
        alias="ips-sniffer-mode",
        default=StatusEnum.DISABLE,
        description="Enable/disable the use of this interface as a one-armed sniffer.",
    )
    ipunnumbered: str = Field(
        default="0.0.0.0",
        description="Unnumbered IP used for PPPoE interfaces for which no unique local address is provided.",
    )
    l2forward: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable l2 forwarding."
    )
    l2tp_client: StatusEnum = Field(
        alias="l2tp-client",
        default=StatusEnum.DISABLE,
        description="Enable/disable this interface as a Layer 2 Tunnelling Protocol (L2TP) client.",
    )
    lacp_ha_slave: StatusEnum = Field(
        alias="lacp-ha-slave", default=StatusEnum.ENABLE, description="LACP HA slave."
    )
    lacp_mode: LacpModeEnum = Field(
        alias="lacp-mode", default=LacpModeEnum.ACTIVE, description="LACP mode."
    )
    lacp_speed: LacpSpeedEnum = Field(
        alias="lacp-speed",
        default=LacpSpeedEnum.SLOW,
        description="How often the interface sends LACP messages.",
    )
    lcp_echo_interval: int = Field(
        alias="lcp-echo-interval",
        default=5,
        description="Time in seconds between PPPoE Link Control Protocol (LCP) echo requests.",
        le=32767,
    )
    lcp_max_echo_fails: int = Field(
        alias="lcp-max-echo-fails",
        default=3,
        description="Maximum missed LCP echo messages before disconnect.",
        le=32767,
    )
    link_up_delay: int = Field(
        alias="link-up-delay",
        default=50,
        description="Number of milliseconds to wait before considering a link is up.",
        le=3600000,
        ge=50,
    )
    lldp_network_policy: str | list | None = Field(
        default=None,
        alias="lldp-network-policy",
        description="LLDP-MED network policy profile.",
    )
    lldp_reception: LldpReceptionEnum = Field(
        alias="lldp-reception",
        default=LldpReceptionEnum.VDOM,
        description="Enable/disable Link Layer Discovery Protocol (LLDP) reception.",
    )
    lldp_transmission: LldpTransmissionEnum = Field(
        alias="lldp-transmission",
        default=LldpTransmissionEnum.VDOM,
        description="Enable/disable Link Layer Discovery Protocol (LLDP) transmission.",
    )
    macaddr: str = Field(
        default="00:00:00:00:00:00", description="Change the interface's MAC address."
    )
    managed_subnetwork_size: ManagedSubnetworkSizeEnum = Field(
        alias="managed-subnetwork-size",
        default=ManagedSubnetworkSizeEnum.S_256,
        description="Number of IP addresses to be allocated by FortiIPAM and used by this FortiGate unit's DHCP server settings.",
    )
    management_ip: str = Field(
        alias="management-ip",
        default="0.0.0.0 0.0.0.0",
        description="High Availability in-band management IP address of this interface.",
    )
    measured_downstream_bandwidth: int = Field(
        alias="measured-downstream-bandwidth",
        default=0,
        description="Measured downstream bandwidth (kbps).",
        le=4294967295,
    )
    measured_upstream_bandwidth: int = Field(
        alias="measured-upstream-bandwidth",
        default=0,
        description="Measured upstream bandwidth (kbps).",
        le=4294967295,
    )
    member: str | list | None = Field(
        default=None,
        description="Physical interfaces that belong to the aggregate or redundant interface.",
    )
    min_links: int = Field(
        alias="min-links",
        default=1,
        description="Minimum number of aggregated ports that must be up.",
        le=32,
        ge=1,
    )
    min_links_down: MinLinksDownEnum = Field(
        alias="min-links-down",
        default=MinLinksDownEnum.OPERATIONAL,
        description="Action to take when less than the configured minimum number of links are active.",
    )
    mode: ModeEnum = Field(
        default=ModeEnum.STATIC, description="Addressing mode (static, DHCP, PPPoE)."
    )
    monitor_bandwidth: StatusEnum = Field(
        alias="monitor-bandwidth",
        default=StatusEnum.DISABLE,
        description="Enable monitoring bandwidth on this interface.",
    )
    mtu: int = Field(
        default=1500, description="MTU value for this interface.", le=4294967295
    )
    mtu_override: StatusEnum = Field(
        alias="mtu-override",
        default=StatusEnum.DISABLE,
        description="Enable to set a custom MTU for this interface.",
    )
    name: str | None = Field(default=None, description="Name.", max_length=15)
    ndiscforward: StatusEnum = Field(
        default=StatusEnum.ENABLE, description="Enable/disable NDISC forwarding."
    )
    netbios_forward: StatusEnum = Field(
        alias="netbios-forward",
        default=StatusEnum.DISABLE,
        description="Enable/disable NETBIOS forwarding.",
    )
    netflow_sampler: NetflowSamplerEnum = Field(
        alias="netflow-sampler",
        default=NetflowSamplerEnum.DISABLE,
        description="Enable/disable NetFlow on this interface and set the data that NetFlow collects (rx, tx, or both).",
    )
    outbandwidth: int = Field(
        default=0,
        description="Bandwidth limit for outgoing traffic (0 - 100000000 kbps).",
        le=80000000,
    )
    padt_retry_timeout: int = Field(
        alias="padt-retry-timeout",
        default=1,
        description="PPPoE Active Discovery Terminate (PADT) used to terminate sessions after an idle time.",
        le=4294967295,
    )
    password: str = Field(
        default="ENC YiN7Aee7bVBtyVrLcurWE8/23NPERCRD6qKbCoN3l4OCEzQc7KIzvBpyBUgTeX9TAsJRccPxwSQEoZEN8mETOd5h/5RSxaiU1VT0c2SXYgjK7/LBK+/n7gRl6C45zCmce+wCMfSucl1M2XMwPMQSBeFGpfeOk1Ke+WfX1Dhg6AM9xwXjV/sJUiE0Q0pCuDwcikESEA==",
        description="PPPoE account's password.",
    )
    polling_interval: int = Field(
        alias="polling-interval",
        default=20,
        description="sFlow polling interval in seconds (1 - 255).",
        le=255,
        ge=1,
    )
    pppoe_unnumbered_negotiate: StatusEnum = Field(
        alias="pppoe-unnumbered-negotiate",
        default=StatusEnum.ENABLE,
        description="Enable/disable PPPoE unnumbered negotiation.",
    )
    pptp_auth_type: PptpAuthTypeEnum = Field(
        alias="pptp-auth-type",
        default=PptpAuthTypeEnum.AUTO,
        description="PPTP authentication type.",
    )
    pptp_client: StatusEnum = Field(
        alias="pptp-client",
        default=StatusEnum.DISABLE,
        description="Enable/disable PPTP client.",
    )
    pptp_password: str = Field(
        alias="pptp-password",
        default="ENC n4AJCvGngCd4joFZpV3Z0PckrsKWzEVjFwtzoChFVlFv7Now8lxuZvPl54MfPWLIj8dW7OXfs8uHCqCYdZQ0MdZdTGs31pCsySq+9DY0zXvFphj6EG/3QkPVj5GVwIY0XGmV3QlKLxG9y8LKYb+sGBdJhTdI9s6HX7B+/7p81x8h0QAccxWVMo3Dq2xvY7pI285KcA==",
        description="PPTP password.",
    )
    pptp_server_ip: str = Field(
        alias="pptp-server-ip", default="0.0.0.0", description="PPTP server IP address."
    )
    pptp_timeout: int = Field(
        alias="pptp-timeout",
        default=0,
        description="Idle timer in minutes (0 for disabled).",
        le=65535,
    )
    pptp_user: str | None = Field(
        default=None, alias="pptp-user", description="PPTP user name.", max_length=64
    )
    preserve_session_route: StatusEnum = Field(
        alias="preserve-session-route",
        default=StatusEnum.DISABLE,
        description="Enable/disable preservation of session route when dirty.",
    )
    priority: int = Field(
        default=1, description="Priority of learned routes.", le=65535, ge=1
    )
    priority_override: StatusEnum = Field(
        alias="priority-override",
        default=StatusEnum.ENABLE,
        description="Enable/disable fail back to higher priority port once recovered.",
    )
    proxy_captive_portal: StatusEnum = Field(
        alias="proxy-captive-portal",
        default=StatusEnum.DISABLE,
        description="Enable/disable proxy captive portal on this interface.",
    )
    reachable_time: int = Field(
        alias="reachable-time",
        default=30000,
        description="IPv4 reachable time in milliseconds (30000 - 3600000, default = 30000).",
        le=3600000,
        ge=30000,
    )
    redundant_interface: str | None = Field(
        default=None, alias="redundant-interface", max_length=15
    )
    remote_ip: str = Field(
        alias="remote-ip",
        default="0.0.0.0 0.0.0.0",
        description="Remote IP address of tunnel.",
    )
    replacemsg_override_group: str | list | None = Field(
        default=None,
        alias="replacemsg-override-group",
        description="Replacement message override group.",
    )
    role: RoleEnum = Field(default=RoleEnum.UNDEFINED, description="Interface role.")
    sample_direction: SampleDirectionEnum = Field(
        alias="sample-direction",
        default=SampleDirectionEnum.BOTH,
        description="Data that NetFlow collects (rx, tx, or both).",
    )
    sample_rate: int = Field(
        alias="sample-rate",
        default=2000,
        description="sFlow sample rate (10 - 99999).",
        le=99999,
        ge=10,
    )
    secondary_ip: StatusEnum = Field(
        alias="secondary-IP",
        default=StatusEnum.DISABLE,
        description="Enable/disable adding a secondary IP to this interface.",
    )
    security_8021x_dynamic_vlan_id: int = Field(
        alias="security-8021x-dynamic-vlan-id",
        default=0,
        description="VLAN ID for virtual switch.",
        le=4094,
    )
    security_8021x_master: str | None = Field(
        default=None,
        alias="security-8021x-master",
        description="802.1X master virtual-switch.",
        max_length=15,
    )
    security_8021x_mode: Security8021xModeEnum = Field(
        alias="security-8021x-mode",
        default=Security8021xModeEnum.DEFAULT,
        description="802.1X mode.",
    )
    security_exempt_list: str | list | None = Field(
        default=None,
        alias="security-exempt-list",
        description="Name of security-exempt-list.",
    )
    security_external_logout: str | None = Field(
        default=None,
        alias="security-external-logout",
        description="URL of external authentication logout server.",
        max_length=127,
    )
    security_external_web: str | None = Field(
        default=None,
        alias="security-external-web",
        description="URL of external authentication web server.",
        max_length=1023,
    )
    security_groups: str | list | None = Field(
        default=None,
        alias="security-groups",
        description="User groups that can authenticate with the captive portal.",
    )
    security_mac_auth_bypass: SecurityMacAuthBypassEnum = Field(
        alias="security-mac-auth-bypass",
        default=SecurityMacAuthBypassEnum.DISABLE,
        description="Enable/disable MAC authentication bypass.",
    )
    security_mode: SecurityModeEnum = Field(
        alias="security-mode",
        default=SecurityModeEnum.NONE,
        description="Turn on captive portal authentication for this interface.",
    )
    security_redirect_url: str | None = Field(
        default=None,
        alias="security-redirect-url",
        description="URL redirection after disclaimer/authentication.",
        max_length=1023,
    )
    service_name: str | None = Field(
        default=None,
        alias="service-name",
        description="PPPoE service name.",
        max_length=63,
    )
    sflow_sampler: StatusEnum = Field(
        alias="sflow-sampler",
        default=StatusEnum.DISABLE,
        description="Enable/disable sFlow on this interface.",
    )
    snmp_index: int = Field(
        alias="snmp-index",
        default=0,
        description="Permanent SNMP Index of the interface.",
        le=2147483647,
        ge=1,
    )
    speed: SpeedEnum = Field(
        default=SpeedEnum.AUTO,
        description="Interface speed. The default setting and the options available depend on the interface hardware.",
    )
    spillover_threshold: int = Field(
        alias="spillover-threshold",
        default=0,
        description="Egress Spillover threshold (0 - 16776000 kbps), 0 means unlimited.",
        le=16776000,
    )
    src_check: StatusEnum = Field(
        alias="src-check",
        default=StatusEnum.ENABLE,
        description="Enable/disable source IP check.",
    )
    status: InterfaceStatusEnum = Field(
        default=InterfaceStatusEnum.UP,
        description="Bring the interface up or shut the interface down.",
    )
    stp: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable STP."
    )
    stp_ha_secondary: StpHaSecondaryEnum = Field(
        alias="stp-ha-secondary",
        default=StpHaSecondaryEnum.PRIORITY_ADJUST,
        description="Control STP behaviour on HA secondary.",
    )
    stpforward: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable STP forwarding."
    )
    stpforward_mode: StpforwardModeEnum = Field(
        alias="stpforward-mode",
        default=StpforwardModeEnum.RPL_ALL_EXT_ID,
        description="Configure STP forwarding mode.",
    )
    subst: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable to always send packets from this interface to a destination MAC address.",
    )
    substitute_dst_mac: str = Field(
        alias="substitute-dst-mac",
        default="00:00:00:00:00:00",
        description="Destination MAC address that all packets are sent to from this interface.",
    )
    swc_first_create: int = Field(
        alias="swc-first-create",
        default=0,
        description="Initial create for switch-controller VLANs.",
        le=4294967295,
    )
    swc_vlan: int = Field(alias="swc-vlan", default=0, le=4294967295)
    switch: str | None = Field(default=None, max_length=15)
    switch_controller_access_vlan: StatusEnum = Field(
        alias="switch-controller-access-vlan",
        default=StatusEnum.DISABLE,
        description="Block FortiSwitch port-to-port traffic.",
    )
    switch_controller_arp_inspection: StatusEnum = Field(
        alias="switch-controller-arp-inspection",
        default=StatusEnum.DISABLE,
        description="Enable/disable FortiSwitch ARP inspection.",
    )
    switch_controller_dhcp_snooping: StatusEnum = Field(
        alias="switch-controller-dhcp-snooping",
        default=StatusEnum.DISABLE,
        description="Switch controller DHCP snooping.",
    )
    switch_controller_dhcp_snooping_option82: StatusEnum = Field(
        alias="switch-controller-dhcp-snooping-option82",
        default=StatusEnum.DISABLE,
        description="Switch controller DHCP snooping option82.",
    )
    switch_controller_dhcp_snooping_verify_mac: StatusEnum = Field(
        alias="switch-controller-dhcp-snooping-verify-mac",
        default=StatusEnum.DISABLE,
        description="Switch controller DHCP snooping verify MAC.",
    )
    switch_controller_dynamic: str | list | None = Field(
        default=None,
        alias="switch-controller-dynamic",
        description="Integrated FortiLink settings for managed FortiSwitch.",
    )
    switch_controller_feature: SwitchControllerFeatureEnum = Field(
        alias="switch-controller-feature",
        default=SwitchControllerFeatureEnum.NONE,
        description="Interface's purpose when assigning traffic (read only).",
    )
    switch_controller_igmp_snooping: StatusEnum = Field(
        alias="switch-controller-igmp-snooping",
        default=StatusEnum.DISABLE,
        description="Switch controller IGMP snooping.",
    )
    switch_controller_igmp_snooping_fast_leave: StatusEnum = Field(
        alias="switch-controller-igmp-snooping-fast-leave",
        default=StatusEnum.DISABLE,
        description="Switch controller IGMP snooping fast-leave.",
    )
    switch_controller_igmp_snooping_proxy: StatusEnum = Field(
        alias="switch-controller-igmp-snooping-proxy",
        default=StatusEnum.DISABLE,
        description="Switch controller IGMP snooping proxy.",
    )
    switch_controller_iot_scanning: StatusEnum = Field(
        alias="switch-controller-iot-scanning",
        default=StatusEnum.DISABLE,
        description="Enable/disable managed FortiSwitch IoT scanning.",
    )
    switch_controller_learning_limit: int = Field(
        alias="switch-controller-learning-limit",
        default=0,
        description="Limit the number of dynamic MAC addresses on this VLAN (1 - 128, 0 = no limit, default).",
        le=128,
    )
    switch_controller_mgmt_vlan: int = Field(
        alias="switch-controller-mgmt-vlan",
        default=4094,
        description="VLAN to use for FortiLink management purposes.",
        le=4094,
        ge=1,
    )
    switch_controller_nac: str | list | None = Field(
        default=None,
        alias="switch-controller-nac",
        description="Integrated FortiLink settings for managed FortiSwitch.",
    )
    switch_controller_rspan_mode: StatusEnum = Field(
        alias="switch-controller-rspan-mode",
        default=StatusEnum.DISABLE,
        description="Stop Layer2 MAC learning and interception of BPDUs and other packets on this interface.",
    )
    switch_controller_source_ip: SwitchControllerSourceIpEnum = Field(
        alias="switch-controller-source-ip",
        default=SwitchControllerSourceIpEnum.OUTBOUND,
        description="Source IP address used in FortiLink over L3 connections.",
    )
    switch_controller_traffic_policy: str | list | None = Field(
        default=None,
        alias="switch-controller-traffic-policy",
        description="Switch controller traffic policy for the VLAN.",
    )
    system_id: str = Field(
        alias="system-id",
        default="00:00:00:00:00:00",
        description="Define a system ID for the aggregate interface.",
    )
    system_id_type: SystemIdTypeEnum = Field(
        alias="system-id-type",
        default=SystemIdTypeEnum.AUTO,
        description="Method in which system ID is generated.",
    )
    tcp_mss: int = Field(
        alias="tcp-mss",
        default=0,
        description="TCP maximum segment size. 0 means do not change segment size.",
        le=65535,
        ge=48,
    )
    trunk: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable VLAN trunk."
    )
    trust_ip_1: str = Field(
        alias="trust-ip-1",
        default="0.0.0.0 0.0.0.0",
        description="Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).",
    )
    trust_ip_2: str = Field(alias="trust-ip-2", default="0.0.0.0 0.0.0.0")
    trust_ip_3: str = Field(alias="trust-ip-3", default="0.0.0.0 0.0.0.0")
    trust_ip6_1: str = Field(
        alias="trust-ip6-1",
        default="::/0",
        description="Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).",
    )
    trust_ip6_2: str = Field(alias="trust-ip6-2", default="::/0")
    trust_ip6_3: str = Field(alias="trust-ip6-3", default="::/0")
    type: TypeEnum = Field(default=TypeEnum.VLAN, description="Interface type.")
    username: str | None = Field(
        default=None,
        description="Username of the PPPoE account, provided by your ISP.",
        max_length=64,
    )
    vdom: str | list = Field(
        default="", description="Interface is in this virtual domain (VDOM)."
    )
    vindex: int = Field(default=0, le=65535)
    vlan_protocol: VlanProtocolEnum = Field(
        alias="vlan-protocol",
        default=VlanProtocolEnum.P_8021Q,
        description="Ethernet protocol of VLAN.",
    )
    vlanforward: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable/disable traffic forwarding between VLANs on this interface.",
    )
    vlanid: int = Field(default=0, description="VLAN ID (1 - 4094).", le=4094, ge=1)
    vrf: int = Field(default=0, description="Virtual Routing Forwarding ID.", le=31)
    vrrp_virtual_mac: StatusEnum = Field(
        alias="vrrp-virtual-mac",
        default=StatusEnum.DISABLE,
        description="Enable/disable use of virtual MAC for VRRP.",
    )
    wccp: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable/disable WCCP on this interface. Used for encapsulated WCCP communication between WCCP clients and servers.",
    )
    weight: int = Field(
        default=0,
        description="Default weight for static routes (if route has no weight configured).",
        le=255,
    )
    wins_ip: str = Field(
        alias="wins-ip", default="0.0.0.0", description="WINS server IP."
    )
    client_options: ClientOptions | None = Field(
        alias="client-options", default=None, description="DHCP client options."
    )
    dhcp_snooping_server_list: DhcpSnoopingServerList | None = Field(
        alias="dhcp-snooping-server-list",
        default=None,
        description="Configure DHCP server access list.",
    )
    ipv6: Ipv6 | None = Field(default=None, description="IPv6 of interface.")
    l2tp_client_settings: L2tpClientSettings | None = Field(
        alias="l2tp-client-settings", default=None, description="L2TP client settings."
    )
    secondaryip: Secondaryip | None = Field(
        default=None, description="Second IP address of interface."
    )
    tagging: Tagging | None = Field(default=None, description="Config object tagging.")
    vrrp: Vrrp | None = Field(default=None, description="VRRP configuration.")


class FortiManagerCreateVlanInterfaceV1(BaseModel, allow_population_by_field_name=True):
    """
    Fortimanager Interface V1 model.
    Notes: At the moment only the vlan interface part has been implemented.
    """

    name: str = Field(description="Interface Name.", max_length=15)
    interface: str | list = Field(description="Interface name.")
    vlanid: int = Field(description="VLAN ID (1 - 4094).", le=4094, ge=1)


class FortiManagerUpdateVlanInterfaceV1(BaseModel, allow_population_by_field_name=True):
    """
    Fortimanager Interface V1 model.
    Notes: At the moment only the vlan interface part has been implemented.
    """

    alias: str | None = Field(
        default=None,
        description="Alias will be displayed with the interface name to make it easier to distinguish.",
        max_length=25,
    )
    vrf: int | None = Field(
        default=0, description="Virtual Routing Forwarding ID.", le=31
    )
    role: RoleEnum | None = Field(
        default=RoleEnum.UNDEFINED, description="Interface role."
    )
    estimated_downstream_bandwidth: int | None = Field(
        alias="estimated-downstream-bandwidth",
        default=0,
        description="Estimated maximum downstream bandwidth (kbps). Used to estimate link utilization.",
        le=4294967295,
    )
    estimated_upstream_bandwidth: int | None = Field(
        alias="estimated-upstream-bandwidth",
        default=0,
        description="Estimated maximum upstream bandwidth (kbps). Used to estimate link utilization.",
        le=4294967295,
    )


class FortiManagerVlanInterfaceV1(
    FortiManagerCreateVlanInterfaceV1,
    FortiManagerUpdateVlanInterfaceV1,
    allow_population_by_field_name=True,
):
    """
    Fortimanager Interface V1 model.
    Notes: At the moment only the vlan interface part has been implemented.
    """

    oid: int | None = Field(default=None, description="Fortinet internal ID.")
    type: TypeEnum = Field(default=TypeEnum.VLAN, description="Interface type.")
    vlan_protocol: VlanProtocolEnum = Field(
        alias="vlan-protocol",
        default=VlanProtocolEnum.P_8021Q,
        description="Ethernet protocol of VLAN.",
    )
