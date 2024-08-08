"""
Pydantic model representing a FortiManager/FortiOS SDWAN template representation
"""

from enum import Enum
from ipaddress import IPv4Address, IPv6Address

from pydantic import BaseModel, Field

# pylint: disable=line-too-long


OBJ_SEQ_ALIAS = "obj seq"


class Status(str, Enum):
    """
    Enum representing the Status
    """

    DISABLE = "disable"  # 0
    ENABLE = "enable"  # 1


class ServiceSlaTieBreak(str, Enum):
    """
    Enum representing the Service Sla Tie Break
    """

    CFG_ORDER = "cfg-order"  # 1
    FIB_BEST_MATCH = "fib-best-match"  # 2
    INPUT_DEVICE = "input-device"  # 3


class AddrMode(str, Enum):
    """
    Enum representing the Addr Mode
    """

    IPV4 = "ipv4"  # 7
    IPV6 = "ipv6"  # 8


class HashMode(str, Enum):
    """
    Enum representing the Hash Mode
    """

    ROUND_ROBIN = "round-robin"  # 1
    SOURCE_IP_BASED = "source-ip-based"  # 2
    SOURCE_DEST_IP_BASED = "source-dest-ip-based"  # 3
    INBANDWIDTH = "inbandwidth"  # 4
    OUTBANDWIDTH = "outbandwidth"  # 5
    BIBANDWIDTH = "bibandwidth"  # 6


class LinkCostFactor(str, Enum):
    """
    Enum representing the Link Cost Factor
    """

    LATENCY = "latency"  # 0
    JITTER = "jitter"  # 1
    PACKET_LOSS = "packet-loss"  # 2
    INBANDWIDTH = "inbandwidth"  # 4
    OUTBANDWIDTH = "outbandwidth"  # 5
    BIBANDWIDTH = "bibandwidth"  # 6
    CUSTOM_PROFILE_1 = "custom-profile-1"  # 7


class ModeService(str, Enum):
    """
    Enum representing the Mode
    """

    AUTO = "auto"  # 0
    MANUAL = "manual"  # 1
    PRIORITY = "priority"  # 3
    SLA = "sla"  # 4


class Role(str, Enum):
    """
    Enum representing the Role
    """

    PRIMARY = "primary"  # 1
    SECONDARY = "secondary"  # 2
    STANDALONE = "standalone"  # 3


class ShortcutPriority(str, Enum):
    """
    Enum representing the Shortcut Priority
    """

    DISABLE = "disable"  # 0
    ENABLE = "enable"  # 1
    AUTO = "auto"  # 2


class SlaCompareMethod(str, Enum):
    """
    Enum representing the Sla Compare Method
    """

    NUMBER = "number"  # 1
    ORDER = "order"  # 0


class TieBreak(str, Enum):
    """
    Enum representing the Tie Break
    """

    ZONE = "zone"  # 1
    CFG_ORDER = "cfg-order"  # 2
    FIB_BEST_MATCH = "fib-best-match"  # 3
    INPUT_DEVICE = "input-device"  # 4


class LoadBalanceMode(str, Enum):
    """
    Enum representing the Load Balance Mode
    """

    SOURCE_IP_BASED = "source-ip-based"  # 1
    WEIGHT_BASED = "weight-based"  # 2
    USAGE_BASED = "usage-based"  # 3
    SOURCE_DEST_IP_BASED = "source-dest-ip-based"  # 4
    MEASURED_VOLUME_BASED = "measured-volume-based"  # 5


class DetectMode(str, Enum):
    """
    Enum representing the Detect Mode
    """

    ACTIVE = "active"  # 1
    PASSIVE = "passive"  # 2
    PREFER_PASSIVE = "prefer-passive"  # 3
    REMOTE = "remote"  # 4
    AGENT_BASED = "agent-based"  # 5


class FtpMode(str, Enum):
    """
    Enum representing the Ftp Mode
    """

    PASSIVE = "passive"  # 0
    PORT = "port"  # 1


class MosCodec(str, Enum):
    """
    Enum representing the Mos Codec
    """

    G711 = "g711"  # 1
    G722 = "g722"  # 2
    G729 = "g729"  # 3


class Protocol(str, Enum):
    """
    Enum representing the Protocol
    """

    PING = "ping"  # 1
    TCP_ECHO = "tcp-echo"  # 2
    UDP_ECHO = "udp-echo"  # 4
    HTTP = "http"  # 8
    TWAMP = "twamp"  # 16
    DNS = "dns"  # 64
    TCP_CONNECT = "tcp-connect"  # 128
    FTP = "ftp"  # 256
    HTTPS = "https"  # 512


class QualityMeasuredMethod(str, Enum):
    """
    Enum representing the Quality Measured Method
    """

    HALF_CLOSE = "half-close"  # 0
    HALF_OPEN = "half-open"  # 1


class SecurityMode(str, Enum):
    """
    Enum representing the Security Mode
    """

    NONE = "none"  # 0
    AUTHENTICATION = "authentication"  # 1


class Mode(str, Enum):
    """
    Enum representing the Mode
    """

    SLA = "sla"  # 1
    SPEEDTEST = "speedtest"  # 2


class LinkCostFactorSla(str, Enum):
    """
    Enum representing the Link Cost Factor Sla
    """

    LATENCY = "latency"  # 1
    JITTER = "jitter"  # 2
    PACKET_LOSS = "packet-loss"  # 4
    MOS = "mos"  # 8


class PacketDuplication(str, Enum):
    """
    Enum representing Packet Duplication
    """

    DISABLE = "disable"  # 0
    FORCE = "force"  # 1
    ON_DEMAND = "on-demand"  # 2


class SlaService(BaseModel):
    """
    Service level agreement (SLA).
    """

    health_check: list[str] = Field(
        ..., alias="health-check", description="SD-WAN health-check."
    )
    id: int = Field(default=0, description="SLA Service id", ge=0, le=4294967295)


class TemplateScopeMember(BaseModel):
    """
    A scope member of SDWAN template (device or device group)
    to which the SDWAN template is applied
    """

    name: str
    vdom: str = "root"


class TemplateType(str, Enum):
    """
    Types of template
    """

    TEMPLATE_SDWAN = "wanprof"


class FortinetSDWANTemplate(BaseModel, alias_by_default=True, use_enum_values=True):
    """
    Pydantic representation of a Fortinet model used for
    SDWANs template management operations
    """

    name: str = Field(
        description="Template SDWAN name.",
    )
    oid: int | None = Field(
        description="Oid of a template SDWAN.",
        default=None,
    )
    scope_member: TemplateScopeMember | None = Field(
        ...,
        description="Template SDWAN scope member setting.",
        alias="scope member",
    )
    description: str | None = Field(
        description="Template SDWAN description.",
        default=None,
    )
    type: TemplateType = TemplateType.TEMPLATE_SDWAN


# SDWAN TEMPLATE ZONE


class Zone(BaseModel, alias_by_default=True, use_enum_values=True):
    """
    Configure SD-WAN zones.
    """

    name: str = Field(..., description="Zone name.", max_length=35)
    obj_seq: int | None = Field(
        alias=OBJ_SEQ_ALIAS,
        default=None,
        description="obj seq of a template SDWAN Zone.",
    )
    oid: int | None = Field(
        description="Oid of a template SDWAN Zone.",
        default=None,
    )
    advpn_health_check: list[str] | None = Field(
        default=None,
        alias="advpn-health-check",
        description="Health check for ADVPN local overlay link quality.",
    )
    advpn_select: Status = Field(
        alias="advpn-select",
        default=Status.DISABLE,
        description="Enable/disable selection of ADVPN based on SDWAN information.",
    )
    minimum_sla_meet_members: int = Field(
        alias="minimum-sla-meet-members",
        default=1,
        description="Minimum number of members which meet SLA when the neighbor is preferred.",
        le=1,
        ge=255,
    )
    service_sla_tie_break: ServiceSlaTieBreak = Field(
        alias="service-sla-tie-break",
        default=ServiceSlaTieBreak.CFG_ORDER,
        description="Method of selecting member if more than one meets the SLA.",
    )


# SDWAN TEMPLATE MEMBERS


class Members(BaseModel, alias_by_default=True):
    """
    FortiGate interfaces added to the SD-WAN.
    """

    oid: int | None = Field(
        description="Oid of a template SDWAN Member.",
        default=None,
    )
    obj_seq: int | None = Field(
        alias=OBJ_SEQ_ALIAS,
        default=None,
        description="Obj seq of a template SDWAN Member.",
    )
    dynamic_member: list[str] = Field(
        alias="_dynamic-member",
        default=[],
        description="Dynamic member of a template SDWAN Member.",
    )
    seq_num: int | None = Field(
        alias="seq-num",
        default=None,
        description="Sequence number(1-512).",
        ge=1,
        le=512,
    )
    interface: list[str] = Field(..., description="Interface name.")
    zone: list[str] = Field(default="virtual-wan-link", description="Zone name.")
    gateway: IPv4Address = Field(
        ...,
        description="The default gateway for this interface. Usually the default gateway of the Internet service provider that this interface is connected to.",
    )
    cost: int = Field(
        default=0,
        description="Cost of this interface for services in SLA mode (0 - 4294967295, default = 0).",
        ge=0,
        le=4294967295,
    )
    priority: int = Field(
        default=1,
        description="Priority of the interface for IPv4 (1 - 65535, default = 1). Used for SD-WAN rules or priority rules.",
        le=65535,
        ge=1,
    )
    status: Status = Field(
        default=Status.ENABLE,
        description="Enable/disable this interface in the SD-WAN.",
    )
    comment: str = Field(..., description="Comments.", max_length=255)
    gateway6: IPv6Address = Field(..., description="IPv6 gateway.")
    ingress_spillover_threshold: int = Field(
        alias="ingress-spillover-threshold",
        default=0,
        description="Ingress spillover threshold for this interface (0 - 16776000 kbit/s). When this traffic volume threshold is reached, new sessions spill over to other interfaces in the SD-WAN.",
        ge=0,
        le=16776000,
    )
    preferred_source: IPv4Address = Field(
        default=...,
        alias="preferred-source",
        description="Preferred source of route for this member.",
    )
    priority6: int = Field(
        default=1024,
        description="Priority of the interface for IPv6 (1 - 65535, default = 1024). Used for SD-WAN rules or priority rules.",
        le=65535,
        ge=1,
    )
    source: IPv4Address = Field(
        ...,
        description="Source IP address used in the health-check packet to the server.",
    )
    source6: IPv6Address = Field(
        ...,
        description="Source IPv6 address used in the health-check packet to the server.",
    )
    spillover_threshold: int = Field(
        alias="spillover-threshold",
        default=0,
        description="Egress spillover threshold for this interface (0 - 16776000 kbit/s). When this traffic volume threshold is reached, new sessions spill over to other interfaces in the SD-WAN.",
        ge=0,
        le=16776000,
    )
    transport_group: int = Field(
        alias="transport-group",
        default=0,
        description="Measured transport group (0 - 255).",
        ge=0,
        le=255,
    )
    volume_ratio: int = Field(
        alias="volume-ratio",
        default=1,
        description="Measured volume ratio (this value / sum of all values = percentage of link volume, 1 - 255).",
        le=255,
        ge=1,
    )
    weight: int = Field(
        default=1,
        description="Weight of this interface for weighted load balancing. (1 - 255) More traffic is directed to interfaces with higher weights.",
        le=255,
        ge=1,
    )


# SDWAN TEMPLATE SERVICE


class Service(BaseModel, alias_by_default=True, use_enum_values=True):
    """
    Create SD-WAN Rules (also called services) to control how sessions are distributed to interfaces in the SD-WAN.
    """

    oid: int | None = Field(
        description="Oid of a template SDWAN Service(Rules).",
        default=None,
    )
    obj_seq: int | None = Field(
        alias=OBJ_SEQ_ALIAS,
        default=None,
        description="Obj seq of a template SDWAN Service(Rules).",
    )
    name: str = Field(..., description="SD-WAN rule name.", max_length=35)
    status: Status = Field(
        default=Status.ENABLE, description="Enable/disable SD-WAN service."
    )
    addr_mode: AddrMode = Field(
        alias="addr-mode",
        default=AddrMode.IPV4,
        description="Address mode (IPv4 or IPv6).",
    )
    src: list[str] | None = Field(..., description="Source address name.")
    groups: list[str] | None = Field(..., description="User groups.")
    dst: list[str] = Field(..., description="Destination address name.")
    internet_service_custom: list[str] | None = Field(
        ...,
        alias="internet-service-custom",
        description="Custom Internet service name list.",
    )
    mode: ModeService = Field(
        default=ModeService.MANUAL,
        description="Control how the SD-WAN rule sets the priority of interfaces in the SD-WAN.",
    )
    src6: list[str] = Field(..., description="Source address6 name.")
    agent_exclusive: Status = Field(
        alias="agent-exclusive",
        default=Status.DISABLE,
        description="Set/unset the service as agent use exclusively.",
    )
    bandwidth_weight: int = Field(
        alias="bandwidth-weight",
        default=0,
        description="Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1.",
        ge=0,
        le=10000000,
    )
    default: Status = Field(
        default=Status.DISABLE,
        description="Enable/disable use of SD-WAN as default service.",
    )
    dscp_forward: Status = Field(
        alias="dscp-forward",
        default=Status.DISABLE,
        description="Enable/disable forward traffic DSCP tag.",
    )
    dscp_forward_tag: str = Field(
        alias="dscp-forward-tag",
        default="000000",
        description="Forward traffic DSCP tag.",
    )
    dscp_reverse: Status = Field(
        alias="dscp-reverse",
        default=Status.DISABLE,
        description="Enable/disable reverse traffic DSCP tag.",
    )
    dscp_reverse_tag: str = Field(
        alias="dscp-reverse-tag",
        default="000000",
        description="Reverse traffic DSCP tag.",
    )
    dst_negate: Status = Field(
        alias="dst-negate",
        default=Status.DISABLE,
        description="Enable/disable negation of destination address match.",
    )
    dst6: list[str] | None = Field(..., description="Destination address6 name.")
    end_port: int = Field(
        alias="end-port",
        default=65535,
        description="End destination port number.",
        ge=0,
        le=65535,
    )
    end_src_port: int = Field(
        alias="end-src-port",
        default=65535,
        description="End source port number.",
        ge=0,
        le=65535,
    )
    gateway: Status = Field(
        default=Status.DISABLE, description="Enable/disable SD-WAN service gateway."
    )
    hash_mode: HashMode = Field(
        alias="hash-mode",
        default=HashMode.ROUND_ROBIN,
        description="Hash algorithm for selected priority members for load balance mode.",
    )
    health_check: list[str] | None = Field(
        ..., alias="health-check", description="Health check list."
    )
    hold_down_time: int = Field(
        alias="hold-down-time",
        default=0,
        description="Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0).",
        ge=0,
        le=10000000,
    )
    id: int = Field(default=0, description="SD-WAN rule ID (1 - 4000).", le=4000, ge=1)
    input_device: list[str] | None = Field(
        ..., alias="input-device", description="Source interface name."
    )
    input_device_negate: Status = Field(
        alias="input-device-negate",
        default=Status.DISABLE,
        description="Enable/disable negation of input device match.",
    )
    input_zone: list[str] | None = Field(
        ..., alias="input-zone", description="Source input-zone name."
    )
    internet_service: Status = Field(
        alias="internet-service",
        default=Status.DISABLE,
        description="Enable/disable use of Internet service for application-based load balancing.",
    )
    internet_service_app_ctrl: list[int] | None = Field(
        ...,
        alias="internet-service-app-ctrl",
        description="Application control based Internet Service ID list.",
    )
    internet_service_app_ctrl_category: list[int] | None = Field(
        ...,
        alias="internet-service-app-ctrl-category",
        description="IDs of one or more application control categories.",
    )
    internet_service_app_ctrl_group: list[str] | None = Field(
        ...,
        alias="internet-service-app-ctrl-group",
        description="Application control based Internet Service group list.",
    )
    internet_service_custom_group: list[str] | None = Field(
        ...,
        alias="internet-service-custom-group",
        description="Custom Internet Service group list.",
    )
    internet_service_group: list[str] | None = Field(
        ..., alias="internet-service-group", description="Internet Service group list."
    )
    internet_service_name: list[str] = Field(
        ..., alias="internet-service-name", description="Internet service name list."
    )
    jitter_weight: int = Field(
        alias="jitter-weight",
        default=0,
        description="Coefficient of jitter in the formula of custom-profile-1.",
        ge=0,
        le=10000000,
    )
    latency_weight: int = Field(
        alias="latency-weight",
        default=0,
        description="Coefficient of latency in the formula of custom-profile-1.",
        ge=0,
        le=10000000,
    )
    link_cost_factor: list[LinkCostFactor] = Field(
        alias="link-cost-factor",
        default=[
            LinkCostFactorSla.LATENCY,
            LinkCostFactorSla.JITTER,
            LinkCostFactorSla.PACKET_LOSS,
        ],
        description="Link cost factor.",
    )
    link_cost_threshold: int = Field(
        alias="link-cost-threshold",
        default=10,
        description="Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10).",
        ge=0,
        le=10000000,
    )
    load_balance: Status = Field(
        alias="load-balance",
        default=Status.DISABLE,
        description="Enable/disable load-balance.",
    )
    minimum_sla_meet_members: int = Field(
        alias="minimum-sla-meet-members",
        default=0,
        description="Minimum number of members which meet SLA.",
        ge=0,
        le=255,
    )
    packet_loss_weight: int = Field(
        alias="packet-loss-weight",
        default=0,
        description="Coefficient of packet-loss in the formula of custom-profile-1.",
        ge=0,
        le=10000000,
    )
    passive_measurement: Status = Field(
        alias="passive-measurement",
        default=Status.DISABLE,
        description="Enable/disable passive measurement based on the service criteria.",
    )
    priority_members: list[str] = Field(
        ...,
        alias="priority-members",
        description="Priority member sequence number list.",
    )
    priority_zone: list[str] = Field(
        ..., alias="priority-zone", description="Priority zone name list."
    )
    protocol: int = Field(default=0, description="Protocol number.", ge=0, le=255)
    quality_link: int = Field(
        alias="quality-link", default=0, description="Quality grade.", ge=0, le=255
    )
    role: Role = Field(
        default=Role.STANDALONE, description="Service role to work with neighbor."
    )
    shortcut: Status = Field(
        default=Status.ENABLE,
        description="Enable/disable shortcut for this service.",
    )
    shortcut_priority: ShortcutPriority = Field(
        alias="shortcut-priority",
        default=ShortcutPriority.AUTO,
        description="High priority of ADVPN shortcut for this service.",
    )
    sla_compare_method: SlaCompareMethod = Field(
        alias="sla-compare-method",
        default=SlaCompareMethod.ORDER,
        description="Method to compare SLA value for SLA mode.",
    )
    sla_stickiness: Status = Field(
        alias="sla-stickiness",
        default=Status.DISABLE,
        description="Enable/disable SLA stickiness (default = disable).",
    )
    src_negate: Status = Field(
        alias="src-negate",
        default=Status.DISABLE,
        description="Enable/disable negation of source address match.",
    )
    standalone_action: Status = Field(
        alias="standalone-action",
        default=Status.DISABLE,
        description="Enable/disable service when selected neighbor role is standalone while service role is not standalone.",
    )
    start_port: int = Field(
        alias="start-port",
        default=1,
        description="Start destination port number.",
        ge=1,
        le=65535,
    )
    start_src_port: int = Field(
        alias="start-src-port",
        default=1,
        description="Start source port number.",
        ge=1,
        le=65535,
    )
    tie_break: TieBreak = Field(
        alias="tie-break",
        default=TieBreak.ZONE,
        description="Method of selecting member if more than one meets the SLA.",
    )
    tos: str = Field(default="0x00", description="Type of service bit pattern.")
    tos_mask: str = Field(
        alias="tos-mask", default="0x00", description="Type of service evaluated bits."
    )
    use_shortcut_sla: Status = Field(
        alias="use-shortcut-sla",
        default=Status.ENABLE,
        description="Enable/disable use of ADVPN shortcut for quality comparison.",
    )
    users: list[str] = Field(..., description="User name.")
    zone_mode: Status = Field(
        alias="zone-mode",
        default=Status.DISABLE,
        description="Enable/disable zone mode.",
    )
    sla: list[SlaService] | None = Field(
        default=None, description="Service level agreement (SLA)."
    )


# SDWAN TEMPLATE NEIGHBOR


class Neighbor(BaseModel):
    """
    Create SD-WAN neighbor from BGP neighbor table to control route advertisements according to SLA status.
    """

    health_check: list[str] = Field(
        ..., alias="health-check", description="SD-WAN health-check name."
    )
    ip: list[IPv4Address] = Field(
        ..., description="IP/IPv6 address of neighbor or neighbor-group name."
    )
    member: list[str] = Field(
        ..., description="SDWAN Neighbor member sequence number list."
    )
    minimum_sla_meet_members: int = Field(
        alias="minimum-sla-meet-members",
        default=1,
        description="Minimum number of members which meet SLA when the neighbor is preferred.",
        le=255,
        ge=1,
    )
    mode: Mode = Field(
        default=Mode.SLA, description="What metric to select the neighbor."
    )
    role: Role = Field(default=Role.STANDALONE, description="Role of neighbor.")
    service_id: list[str] | None = Field(
        ...,
        alias="service-id",
        description="SD-WAN service ID to work with the neighbor.",
    )
    sla_id: int | None = Field(
        alias="sla-id",
        default=None,
        description="SLA id associated to a SDWAN Neighbor Sub Object",
        ge=1,
        le=4294967295,
    )


# SDWAN TEMPLATE PERFORMANCE SLA TARGET


class Sla(BaseModel):
    """
    Service level agreement (SLA).
    """

    id: int = Field(..., description="SDWAN SLA id", le=32, ge=0)
    jitter_threshold: int = Field(
        alias="jitter-threshold",
        default=5,
        description="Jitter for SLA to make decision in milliseconds. (0 - 10000000, default = 5).",
        ge=0,
        le=10000000,
    )
    latency_threshold: int = Field(
        alias="latency-threshold",
        default=5,
        description="Latency for SLA to make decision in milliseconds. (0 - 10000000, default = 5).",
        ge=0,
        le=10000000,
    )
    link_cost_factor: list[LinkCostFactorSla] = Field(
        default=[
            LinkCostFactorSla.LATENCY,
            LinkCostFactorSla.JITTER,
            LinkCostFactorSla.PACKET_LOSS,
        ],
        alias="link-cost-factor",
        description="Criteria on which to base link selection.",
    )
    mos_threshold: str = Field(
        alias="mos-threshold",
        default="3.6",
        description="Minimum Mean Opinion Score for SLA to be marked as pass. (1.0 - 5.0, default = 3.6).",
        max_length=35,
    )
    packetloss_threshold: int = Field(
        alias="packetloss-threshold",
        default=0,
        description="Packet loss for SLA to make decision in percentage. (0 - 100, default = 0).",
        ge=0,
        le=100,
    )
    priority_in_sla: int = Field(
        alias="priority-in-sla",
        default=0,
        description="Value to be distributed into routing table when in-sla (0 - 65535, default = 0).",
        ge=0,
        le=65535,
    )
    priority_out_sla: int = Field(
        alias="priority-out-sla",
        default=0,
        description="Value to be distributed into routing table when out-sla (0 - 65535, default = 0).",
        ge=0,
        le=65535,
    )


# SDWAN TEMPLATE PERFORMANCE SLA


class HealthCheck(BaseModel):
    """
    SD-WAN status checking or health checking. Identify a server on the Internet and determine how SD-WAN verifies that the FortiGate can communicate with it.
    """

    addr_mode: AddrMode = Field(
        alias="addr-mode",
        default=AddrMode.IPV4,
        description="Address mode (IPv4 or IPv6).",
    )
    class_id: list[str] = Field(..., alias="class-id", description="Traffic class ID.")
    detect_mode: DetectMode = Field(
        alias="detect-mode",
        default=DetectMode.ACTIVE,
        description="The mode determining how to detect the server.",
    )
    diffservcode: str = Field(
        default="000000",
        description="Differentiated services code point (DSCP) in the IP header of the probe packet.",
    )
    dns_match_ip: IPv4Address = Field(
        ...,
        alias="dns-match-ip",
        description="Response IP expected from DNS server if the protocol is DNS.",
    )
    dns_request_domain: str = Field(
        alias="dns-request-domain",
        default="www.example.com",
        description="Fully qualified domain name to resolve for the DNS probe.",
        max_length=255,
    )
    embed_measured_health: Status = Field(
        alias="embed-measured-health",
        default=Status.DISABLE,
        description="Enable/disable embedding measured health information.",
    )
    failtime: int = Field(
        default=5,
        description="Number of failures before server is considered lost (1 - 3600, default = 5).",
        le=3600,
        ge=1,
    )
    ftp_file: str | None = Field(
        ...,
        alias="ftp-file",
        description="Full path and file name on the FTP server to download for FTP health-check to probe.",
        max_length=254,
    )
    ftp_mode: FtpMode = Field(
        alias="ftp-mode", default=FtpMode.PASSIVE, description="FTP mode."
    )
    ha_priority: int = Field(
        alias="ha-priority",
        default=1,
        description="HA election priority (1 - 50).",
        le=50,
        ge=1,
    )
    http_agent: str = Field(
        alias="http-agent",
        default="Chrome/ Safari/",
        description="String in the http-agent field in the HTTP header.",
        max_length=1024,
    )
    http_get: str = Field(
        alias="http-get",
        default="/",
        description="URL used to communicate with the server if the protocol if the protocol is HTTP.",
        max_length=1024,
    )
    http_match: str | None = Field(
        ...,
        alias="http-match",
        description="Response string expected from the server if the protocol is HTTP.",
        max_length=1024,
    )
    interval: int = Field(
        default=500,
        description="Status check interval in milliseconds, or the time between attempting to connect to the server (20 - 3600*1000 msec, default = 500).",
        le=3600000,
        ge=20,
    )
    members: list[str] = Field(
        ..., description="SDWAN Performance SLA member sequence number list."
    )
    mos_codec: MosCodec = Field(
        alias="mos-codec",
        default=MosCodec.G711,
        description="Codec to use for MOS calculation (default = g711).",
    )
    name: str = Field(
        ..., description="Status check or health check name.", max_length=35
    )
    packet_size: int = Field(
        alias="packet-size",
        default=124,
        description="Packet size of a TWAMP test session. (124/158 - 1024)",
    )
    password: str = Field(
        ...,
        description="TWAMP controller password in authentication mode.",
    )
    port: int = Field(
        default=0,
        description="Port number used to communicate with the server over the selected protocol (0 - 65535, default = 0, auto select. http, tcp-connect: 80, udp-echo, tcp-echo: 7, dns: 53, ftp: 21, twamp: 862).",
        ge=0,
        le=65535,
    )
    probe_count: int = Field(
        alias="probe-count",
        default=30,
        description="Number of most recent probes that should be used to calculate latency and jitter (5 - 30, default = 30).",
        le=30,
        ge=5,
    )
    probe_packets: Status = Field(
        alias="probe-packets",
        default=Status.ENABLE,
        description="Enable/disable transmission of probe packets.",
    )
    probe_timeout: int = Field(
        alias="probe-timeout",
        default=500,
        description="Time to wait before a probe packet is considered lost (20 - 3600*1000 msec, default = 500).",
        le=3600000,
        ge=20,
    )
    protocol: Protocol = Field(
        default=Protocol.PING,
        description="Protocol used to determine if the FortiGate can communicate with the server.",
    )
    quality_measured_method: QualityMeasuredMethod = Field(
        alias="quality-measured-method",
        default=QualityMeasuredMethod.HALF_OPEN,
        description="Method to measure the quality of tcp-connect.",
    )
    recoverytime: int = Field(
        default=5,
        description="Number of successful responses received before server is considered recovered (1 - 3600, default = 5).",
        le=3600,
        ge=1,
    )
    security_mode: SecurityMode = Field(
        alias="security-mode",
        default=SecurityMode.NONE,
        description="Twamp controller security mode.",
    )
    server: list[IPv4Address] = Field(
        ..., description="IP address or FQDN name of the server."
    )
    sla_fail_log_period: int = Field(
        alias="sla-fail-log-period",
        default=0,
        description="Time interval in seconds that SLA fail log messages will be generated (0 - 3600, default = 0).",
        ge=0,
        le=3600,
    )
    sla_id_redistribute: int = Field(
        alias="sla-id-redistribute",
        default=0,
        description="Select the ID from the SLA sub-table. The selected SLA's priority value will be distributed into the routing table (0 - 32, default = 0).",
        ge=0,
        le=32,
    )
    sla_pass_log_period: int = Field(
        alias="sla-pass-log-period",
        default=0,
        description="Time interval in seconds that SLA pass log messages will be generated (0 - 3600, default = 0).",
        ge=0,
        le=3600,
    )
    source: IPv4Address = Field(
        ...,
        description="Source IP address used in the health-check packet to the server.",
    )
    source6: IPv6Address = Field(
        ...,
        description="Source IPv6 address used in the health-check packet to server.",
    )
    system_dns: Status = Field(
        alias="system-dns",
        default=Status.DISABLE,
        description="Enable/disable system DNS as the probe server.",
    )
    threshold_alert_jitter: int = Field(
        alias="threshold-alert-jitter",
        default=0,
        description="Alert threshold for jitter (ms, default = 0).",
        ge=0,
        le=4294967295,
    )
    threshold_alert_latency: int = Field(
        alias="threshold-alert-latency",
        default=0,
        description="Alert threshold for latency (ms, default = 0).",
        ge=0,
        le=4294967295,
    )
    threshold_alert_packetloss: int = Field(
        alias="threshold-alert-packetloss",
        default=0,
        description="Alert threshold for packet loss (percentage, default = 0).",
        ge=0,
        le=100,
    )
    threshold_warning_jitter: int = Field(
        alias="threshold-warning-jitter",
        default=0,
        description="Warning threshold for jitter (ms, default = 0).",
        ge=0,
        le=4294967295,
    )
    threshold_warning_latency: int = Field(
        alias="threshold-warning-latency",
        default=0,
        description="Warning threshold for latency (ms, default = 0).",
        ge=0,
        le=4294967295,
    )
    threshold_warning_packetloss: int = Field(
        alias="threshold-warning-packetloss",
        default=0,
        description="Warning threshold for packet loss (percentage, default = 0).",
        ge=0,
        le=100,
    )
    update_cascade_interface: Status = Field(
        alias="update-cascade-interface",
        default=Status.ENABLE,
        description="Enable/disable update cascade interface.",
    )
    update_static_route: Status = Field(
        alias="update-static-route",
        default=Status.ENABLE,
        description="Enable/disable updating the static route.",
    )
    user: str | None = Field(
        ..., description="The user name to access probe server.", max_length=64
    )
    vrf: int = Field(
        default=0, description="Virtual Routing Forwarding ID.", ge=0, le=251
    )
    sla: list[Sla] | None = Field(
        default=None, description="Service level agreement (SLA)."
    )


# SDWAN TEMPLATE DUPLICATION


class Duplication(BaseModel):
    """
    Create SD-WAN duplication rule.
    """

    dstaddr: list[str] = Field(
        ..., description="Destination address or address group names."
    )
    dstaddr6: list[str] = Field(
        ..., description="Destination address6 or address6 group names."
    )
    dstintf: list[str] = Field(
        ..., description="Outgoing (egress) interfaces or zones."
    )
    id: int = Field(..., description="Duplication rule ID (1 - 255).", le=255, ge=1)
    packet_de_duplication: Status = Field(
        alias="packet-de-duplication",
        default=Status.DISABLE,
        description="Enable/disable discarding of packets that have been duplicated.",
    )
    packet_duplication: PacketDuplication = Field(
        alias="packet-duplication",
        default=PacketDuplication.DISABLE,
        description="Configure packet duplication method.",
    )
    service: list[str] = Field(..., description="Service and service group name.")
    service_id: list[str] = Field(
        ..., alias="service-id", description="SD-WAN service rule ID list."
    )
    sla_match_service: Status = Field(
        alias="sla-match-service",
        default=Status.DISABLE,
        description="Enable/disable packet duplication matching health-check SLAs in service rule.",
    )
    srcaddr: list[str] = Field(
        ..., description="Source address or address group names."
    )
    srcaddr6: list[str] = Field(
        ..., description="Source address6 or address6 group names."
    )
    srcintf: list[str] = Field(
        ..., description="Incoming (ingress) interfaces or zones."
    )


# SDWAN TEMPLATE ADVANCED OPTION


class FortinetSDWANTemplateAdvancedOption(BaseModel):
    """
    Configure redundant Internet connections with multiple outbound links and health-check profiles.
    """

    app_perf_log_period: int = Field(
        alias="app-perf-log-period",
        default=0,
        description="Time interval in seconds that application performance logs are generated (0 - 3600, default = 0).",
        ge=0,
        le=3600,
    )
    duplication_max_num: int = Field(
        alias="duplication-max-num",
        default=2,
        description="Maximum number of interface members a packet is duplicated in the SD-WAN zone (2 - 4, default = 2; if set to 3, the original packet plus 2 more copies are created).",
        le=4,
        ge=2,
    )
    fail_alert_interfaces: list[str] = Field(
        ...,
        alias="fail-alert-interfaces",
        description="Physical interfaces that will be alerted.",
    )
    fail_detect: Status = Field(
        alias="fail-detect",
        default=Status.DISABLE,
        description="Enable/disable SD-WAN Internet connection status checking (failure detection).",
    )
    load_balance_mode: LoadBalanceMode = Field(
        alias="load-balance-mode",
        default=LoadBalanceMode.SOURCE_IP_BASED,
        description="Algorithm or mode to use for load balancing Internet traffic to SD-WAN members.",
    )
    neighbor_hold_boot_time: int = Field(
        alias="neighbor-hold-boot-time",
        default=0,
        description="Waiting period in seconds when switching from the primary neighbor to the secondary neighbor from the neighbor start. (0 - 10000000, default = 0).",
        ge=0,
        le=10000000,
    )
    neighbor_hold_down: Status = Field(
        alias="neighbor-hold-down",
        default=Status.DISABLE,
        description="Enable/disable hold switching from the secondary neighbor to the primary neighbor.",
    )
    neighbor_hold_down_time: int = Field(
        alias="neighbor-hold-down-time",
        default=0,
        description="Waiting period in seconds when switching from the secondary neighbor to the primary neighbor when hold-down is disabled. (0 - 10000000, default = 0).",
        ge=0,
        le=10000000,
    )
    speedtest_bypass_routing: Status = Field(
        alias="speedtest-bypass-routing",
        default=Status.DISABLE,
        description="Enable/disable bypass routing when speedtest on a SD-WAN member.",
    )
    status: Status = Field(default=Status.DISABLE, description="Enable/disable SD-WAN.")
    health_check: list[HealthCheck] = Field(
        ...,
        alias="health-check",
        description="SD-WAN status checking or health checking. Identify a server on the Internet and determine how SD-WAN verifies that the FortiGate can communicate with it.",
    )
    duplication: list[Duplication] = Field(
        ..., description="Create SD-WAN duplication rule."
    )
    members: list[Members] = Field(
        ..., description="FortiGate interfaces added to the SD-WAN."
    )
    neighbor: list[Neighbor] = Field(
        ...,
        description="Create SD-WAN neighbor from BGP neighbor table to control route advertisements according to SLA status.",
    )
    service: list[Service] = Field(
        ...,
        description="Create SD-WAN rules (also called services) to control how sessions are distributed to interfaces in the SD-WAN.",
    )
    zone: list[Zone] = Field(..., description="Configure SD-WAN zones.")
