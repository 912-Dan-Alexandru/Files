"""
Fortimanager firewall policy rule model
"""

# pylint: disable=line-too-long, too-many-lines
from pydantic import BaseModel, Field

from common.southbound.fortimanager.v1.models.policy_package.rules.common.enums import (
    ActionEnum,
    FirewallSessionDirtyEnum,
    GeoipMatchEnum,
    InspectionModeEnum,
    LogtrafficEnum,
    ReputationDirectionEnum,
    StatusEnum,
    TcpSessionWithoutSynEnum,
    WanoptDetectionEnum,
    WanoptPassiveOptEnum,
    ZtnaTagsMatchLogicEnum,
)
from common.southbound.fortimanager.v1.models.policy_package.rules.security_policy import (
    FirewallSecurityPolicyCommonProps,
)


class FirewallPolicy(BaseModel):
    """
    Configure IPv4/IPv6 policies.
    """

    casb_profile: list[str] = Field(
        ..., alias="casb-profile", description="Name of an existing CASB profile."
    )

    diameter_filter_profile: list[str] = Field(
        ...,
        alias="diameter-filter-profile",
        description="Name of an existing Diameter filter profile.",
    )

    pcp_inbound: StatusEnum = Field(
        alias="pcp-inbound",
        default=StatusEnum.DISABLE,
        description="Enable/disable PCP inbound DNAT.",
    )
    pcp_outbound: StatusEnum = Field(
        alias="pcp-outbound",
        default=StatusEnum.DISABLE,
        description="Enable/disable PCP outbound SNAT.",
    )
    pcp_poolname: list[str] = Field(
        ..., alias="pcp-poolname", description="PCP pool names."
    )

    ztna_ems_tag_secondary: list[str] = Field(
        ...,
        alias="ztna-ems-tag-secondary",
        description="Source ztna-ems-tag-secondary names.",
    )


class FirewallPolicyCommonProps(FirewallSecurityPolicyCommonProps):
    """
    Configure IPv4/IPv6 policies common properties.
    """

    anti_replay: StatusEnum = Field(
        alias="anti-replay",
        default=StatusEnum.ENABLE,
        description="Enable/disable anti-replay check.",
    )
    auth_cert: list[str] = Field(
        ...,
        alias="auth-cert",
        description="HTTPS server certificate for policy authentication.",
    )
    auth_path: StatusEnum = Field(
        alias="auth-path",
        default=StatusEnum.DISABLE,
        description="Enable/disable authentication-based routing.",
    )
    auth_redirect_addr: str = Field(
        ...,
        alias="auth-redirect-addr",
        description="HTTP-to-HTTPS redirect address for firewall authentication.",
        max_length=63,
    )
    auto_asic_offload: StatusEnum = Field(
        alias="auto-asic-offload",
        default=StatusEnum.ENABLE,
        description="Enable/disable policy traffic ASIC offloading.",
    )

    block_notification: StatusEnum = Field(
        alias="block-notification",
        default=StatusEnum.DISABLE,
        description="Enable/disable block notification.",
    )
    captive_portal_exempt: StatusEnum = Field(
        alias="captive-portal-exempt",
        default=StatusEnum.DISABLE,
        description="Enable to exempt some users from the captive portal.",
    )
    capture_packet: StatusEnum = Field(
        alias="capture-packet",
        default=StatusEnum.DISABLE,
        description="Enable/disable capture packets.",
    )

    cgn_eif: StatusEnum = Field(
        alias="cgn-eif",
        default=StatusEnum.DISABLE,
        description="Enable/Disable CGN endpoint independent filtering.",
    )
    cgn_eim: StatusEnum = Field(
        alias="cgn-eim",
        default=StatusEnum.DISABLE,
        description="Enable/Disable CGN endpoint independent mapping",
    )
    cgn_log_server_grp: str = Field(
        ...,
        alias="cgn-log-server-grp",
        description="NP log server group name",
        max_length=35,
    )
    cgn_resource_quota: int = Field(
        alias="cgn-resource-quota",
        default=16,
        description="resource quota",
        le=16,
        ge=1,
    )
    cgn_session_quota: int = Field(
        alias="cgn-session-quota",
        default=16777215,
        description="session quota",
        le=16777215,
    )

    custom_log_fields: list[str] = Field(
        ...,
        alias="custom-log-fields",
        description="Custom fields to append to log messages for this policy.",
    )
    decrypted_traffic_mirror: list[str] = Field(
        ..., alias="decrypted-traffic-mirror", description="Decrypted traffic mirror."
    )
    delay_tcp_npu_session: StatusEnum = Field(
        alias="delay-tcp-npu-session",
        default=StatusEnum.DISABLE,
        description="Enable TCP NPU session delay to guarantee packet order"
        " of 3-way handshake.",
    )

    diffserv_copy: StatusEnum = Field(
        alias="diffserv-copy",
        default=StatusEnum.DISABLE,
        description="Enable to copy packet's DiffServ values from session's"
        " original direction to its reply direction.",
    )
    diffserv_forward: StatusEnum = Field(
        alias="diffserv-forward",
        default=StatusEnum.DISABLE,
        description="Enable to change packet's DiffServ values to the specified "
        "diffservcode-forward value.",
    )
    diffserv_reverse: StatusEnum = Field(
        alias="diffserv-reverse",
        default=StatusEnum.DISABLE,
        description="Enable to change packet's reverse (reply) DiffServ values"
        " to the specified diffservcode-rev value.",
    )
    diffservcode_forward: str = Field(
        alias="diffservcode-forward",
        default="000000",
        description="Change packet's DiffServ to this value.",
    )
    diffservcode_rev: str = Field(
        alias="diffservcode-rev",
        default="000000",
        description="Change packet's reverse (reply) DiffServ to this value.",
    )
    disclaimer: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable/disable user authentication disclaimer.",
    )

    dsri: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable DSRI to ignore HTTP server responses.",
    )

    dynamic_shaping: StatusEnum = Field(
        alias="dynamic-shaping",
        default=StatusEnum.DISABLE,
        description="Enable/disable dynamic RADIUS defined traffic shaping.",
    )
    email_collect: StatusEnum = Field(
        alias="email-collect",
        default=StatusEnum.DISABLE,
        description="Enable/disable email collection.",
    )

    fec: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable/disable Forward Error Correction on traffic matching"
        " this policy on a FEC device.",
    )

    firewall_session_dirty: FirewallSessionDirtyEnum = Field(
        alias="firewall-session-dirty",
        default=FirewallSessionDirtyEnum.CHECK_ALL,
        description="How to handle sessions if the configuration of this "
        "firewall policy changes.",
    )
    fixedport: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable to prevent source NAT from changing a session's "
        "source port.",
    )
    fsso_agent_for_ntlm: list[str] = Field(
        ...,
        alias="fsso-agent-for-ntlm",
        description="FSSO agent to use for NTLM authentication.",
    )

    geoip_anycast: StatusEnum = Field(
        alias="geoip-anycast",
        default=StatusEnum.DISABLE,
        description="Enable/disable recognition of anycast IP addresses using the"
        " geography IP database.",
    )
    geoip_match: GeoipMatchEnum = Field(
        alias="geoip-match",
        default=GeoipMatchEnum.PHYSICAL_LOCATION,
        description="Match geography address based either on its physical location"
        " or registered location.",
    )

    http_policy_redirect: StatusEnum = Field(
        alias="http-policy-redirect",
        default=StatusEnum.DISABLE,
        description="Redirect HTTP(S) traffic to matching transparent web proxy"
        " policy.",
    )

    identity_based_route: list[str] = Field(
        ...,
        alias="identity-based-route",
        description="Name of identity-based routing rule.",
    )
    inbound: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Policy-based IPsec VPN: only traffic from"
        " the remote network can initiate a VPN.",
    )
    inspection_mode: InspectionModeEnum = Field(
        alias="inspection-mode",
        default=InspectionModeEnum.FLOW,
        description="Policy inspection mode (Flow/proxy). Default is Flow mode.",
    )

    ip_version_type: str = Field(
        alias="ip-version-type", default="ipv4", description="IP version of the policy."
    )
    ippool: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable to use IP Pools for source NAT."
    )

    label: str = Field(
        ...,
        description="Label for the policy that appears when the GUI is in Section "
        "View mode.",
        max_length=63,
    )

    logtraffic_start: StatusEnum = Field(
        alias="logtraffic-start",
        default=StatusEnum.DISABLE,
        description="Record logs when a session starts.",
    )
    match_vip: StatusEnum = Field(
        alias="match-vip",
        default=StatusEnum.ENABLE,
        description="Enable to match packets that have had their destination addresses"
        " changed by a VIP.",
    )
    match_vip_only: StatusEnum = Field(
        alias="match-vip-only",
        default=StatusEnum.DISABLE,
        description="Enable/disable matching of only those packets that have had "
        "their destination addresses changed by a VIP.",
    )

    nat: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable source NAT."
    )

    natinbound: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Policy-based IPsec VPN: apply destination NAT to inbound traffic.",
    )
    natip: str | list[str] = Field(
        default="0.0.0.0 0.0.0.0",
        description="Policy-based IPsec VPN: source NAT IP address for outgoing"
        " traffic.",
    )
    natoutbound: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Policy-based IPsec VPN: apply source NAT to outbound traffic.",
    )
    network_service_dynamic: list[str] = Field(
        ...,
        alias="network-service-dynamic",
        description="Dynamic Network Service name.",
    )
    network_service_src_dynamic: list[str] = Field(
        ...,
        alias="network-service-src-dynamic",
        description="Dynamic Network Service source name.",
    )
    np_acceleration: StatusEnum = Field(
        alias="np-acceleration",
        default=StatusEnum.ENABLE,
        description="Enable/disable UTM Network Processor acceleration.",
    )
    ntlm: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable NTLM authentication."
    )
    ntlm_enabled_browsers: list[str] = Field(
        ...,
        alias="ntlm-enabled-browsers",
        description="HTTP-User-Agent value of supported browsers.",
    )
    ntlm_guest: StatusEnum = Field(
        alias="ntlm-guest",
        default=StatusEnum.DISABLE,
        description="Enable/disable NTLM guest user access.",
    )
    outbound: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        description="Policy-based IPsec VPN: only traffic from the internal"
        " network can initiate a VPN.",
    )
    passive_wan_health_measurement: StatusEnum = Field(
        alias="passive-wan-health-measurement",
        default=StatusEnum.DISABLE,
        description="Enable/disable passive WAN health measurement. "
        "When enabled, auto-asic-offload is disabled.",
    )

    per_ip_shaper: list[str] = Field(
        ..., alias="per-ip-shaper", description="Per-IP traffic shaper."
    )
    permit_any_host: StatusEnum = Field(
        alias="permit-any-host",
        default=StatusEnum.DISABLE,
        description="Accept UDP packets from any host.",
    )
    permit_stun_host: StatusEnum = Field(
        alias="permit-stun-host",
        default=StatusEnum.DISABLE,
        description="Accept UDP packets from any Session Traversal Utilities"
        " for NAT (STUN) host.",
    )
    policy_behaviour_type: str = Field(
        alias="policy-behaviour-type",
        default="standard",
        description="Behaviour of the policy.",
    )
    policy_expiry: StatusEnum = Field(
        alias="policy-expiry",
        default=StatusEnum.DISABLE,
        description="Enable/disable policy expiry.",
    )
    policy_expiry_date: str = Field(
        alias="policy-expiry-date",
        default="0000-00-00 00:00:00",
        description="Policy expiry date (YYYY-MM-DD HH:MM:SS).",
    )
    policy_expiry_date_utc: str = Field(
        ...,
        alias="policy-expiry-date-utc",
        description="Policy expiry date and time, in epoch format.",
    )
    policy_offload: StatusEnum = Field(
        alias="policy-offload",
        default=StatusEnum.ENABLE,
        description="Enable/Disable hardware session setup for CGNAT.",
    )

    poolname: list[str] = Field(..., description="IP Pool names.")
    poolname6: list[str] = Field(..., description="IPv6 pool names.")

    radius_mac_auth_bypass: StatusEnum = Field(
        alias="radius-mac-auth-bypass",
        default=StatusEnum.DISABLE,
        description="Enable MAC authentication bypass. The bypassed MAC address must"
        " be received from RADIUS server.",
    )
    redirect_url: str = Field(
        ...,
        alias="redirect-url",
        description="URL users are directed to after seeing and accepting the "
        "disclaimer or authenticating.",
        max_length=1023,
    )
    replacemsg_override_group: list[str] = Field(
        ...,
        alias="replacemsg-override-group",
        description="Override the default replacement message group for this policy.",
    )
    reputation_direction: ReputationDirectionEnum = Field(
        alias="reputation-direction",
        default=ReputationDirectionEnum.DESTINATION,
        description="Direction of the initial traffic for reputation to take effect.",
    )
    reputation_direction6: ReputationDirectionEnum = Field(
        alias="reputation-direction6",
        default=ReputationDirectionEnum.DESTINATION,
        description="Direction of the initial traffic for IPv6 reputation to take"
        " effect.",
    )
    reputation_minimum: int = Field(
        alias="reputation-minimum",
        default=0,
        description="Minimum Reputation to take action.",
        le=4294967295,
    )
    reputation_minimum6: int = Field(
        ...,
        alias="reputation-minimum6",
        description="IPv6 Minimum Reputation to take action.",
        le=4294967295,
    )
    rtp_addr: list[str] = Field(
        ...,
        alias="rtp-addr",
        description="Address names if this is an RTP NAT policy.",
    )
    rtp_nat: StatusEnum = Field(
        alias="rtp-nat",
        default=StatusEnum.DISABLE,
        description="Enable Real Time Protocol (RTP) NAT.",
    )

    schedule_timeout: StatusEnum = Field(
        alias="schedule-timeout",
        default=StatusEnum.DISABLE,
        description="Enable to force current sessions to end when the schedule"
        " object times out. Disable allows them to end from inactivity.",
    )

    session_ttl: str = Field(
        alias="session-ttl",
        default="0",
        description="TTL in seconds for sessions accepted by this policy"
        " (0 means use the system default session TTL).",
    )
    sgt: list[int] = Field(..., description="Security group tags.")
    sgt_check: StatusEnum = Field(
        alias="sgt-check",
        default=StatusEnum.DISABLE,
        description="Enable/disable security group tags (SGT) check.",
    )
    src_vendor_mac: list[str] = Field(
        ..., alias="src-vendor-mac", description="Vendor MAC source ID."
    )

    ssh_policy_redirect: StatusEnum = Field(
        alias="ssh-policy-redirect",
        default=StatusEnum.DISABLE,
        description="Redirect SSH traffic to matching transparent proxy policy.",
    )
    ssl_ssh_profile: list[str] = Field(
        alias="ssl-ssh-profile",
        default="no-inspection",
        description="Name of an existing SSL SSH profile.",
    )

    tcp_mss_receiver: int = Field(
        alias="tcp-mss-receiver",
        default=0,
        description="Receiver TCP maximum segment size (MSS).",
        le=65535,
    )
    tcp_mss_sender: int = Field(
        alias="tcp-mss-sender",
        default=0,
        description="Sender TCP maximum segment size (MSS).",
        le=65535,
    )
    tcp_session_without_syn: TcpSessionWithoutSynEnum = Field(
        alias="tcp-session-without-syn",
        default=TcpSessionWithoutSynEnum.DISABLE,
        description="Enable/disable creation of TCP session without SYN flag.",
    )
    tcp_timeout_pid: list[str] = Field(
        ..., alias="tcp-timeout-pid", description="TCP timeout profile ID"
    )
    timeout_send_rst: StatusEnum = Field(
        alias="timeout-send-rst",
        default=StatusEnum.DISABLE,
        description="Enable/disable sending RST packets when TCP sessions expire.",
    )
    tos: str = Field(
        default="0x00", description="ToS (Type of Service) value used for comparison."
    )
    tos_mask: str = Field(
        alias="tos-mask",
        default="0x00",
        description="Non-zero bit positions are used for comparison while "
        "zero bit positions are ignored.",
    )
    tos_negate: StatusEnum = Field(
        alias="tos-negate",
        default=StatusEnum.DISABLE,
        description="Enable negated TOS match.",
    )
    traffic_shaper: list[str] = Field(
        ..., alias="traffic-shaper", description="Traffic shaper."
    )
    traffic_shaper_reverse: list[str] = Field(
        ..., alias="traffic-shaper-reverse", description="Reverse traffic shaper."
    )
    udp_timeout_pid: list[str] = Field(
        ..., alias="udp-timeout-pid", description="UDP timeout profile ID"
    )

    vlan_cos_fwd: int = Field(
        alias="vlan-cos-fwd",
        default=255,
        description="VLAN forward direction user priority: "
        "255 passthrough, 0 lowest, 7 highest.",
        le=7,
    )
    vlan_cos_rev: int = Field(
        alias="vlan-cos-rev",
        default=255,
        description="VLAN reverse direction user priority: "
        "255 passthrough, 0 lowest, 7 highest.",
        le=7,
    )
    vlan_filter: str = Field(
        ..., alias="vlan-filter", description="VLAN ranges to allow"
    )

    vpntunnel: list[str] = Field(
        ..., description="Policy-based IPsec VPN: name of the IPsec VPN Phase 1."
    )
    waf_profile: list[str] = Field(
        ...,
        alias="waf-profile",
        description="Name of an existing Web application firewall profile.",
    )
    wanopt: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable WAN optimization."
    )
    wanopt_detection: WanoptDetectionEnum = Field(
        alias="wanopt-detection",
        default=WanoptDetectionEnum.ACTIVE,
        description="WAN optimization auto-detection mode.",
    )
    wanopt_passive_opt: WanoptPassiveOptEnum = Field(
        alias="wanopt-passive-opt",
        default=WanoptPassiveOptEnum.DEFAULT,
        description="WAN optimization passive mode options. "
        "This option decides what IP address will be used to connect server.",
    )
    wanopt_peer: list[str] = Field(
        ..., alias="wanopt-peer", description="WAN optimization peer."
    )
    wanopt_profile: list[str] = Field(
        ..., alias="wanopt-profile", description="WAN optimization profile."
    )
    wccp: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable/disable forwarding traffic matching "
        "this policy to a configured WCCP server.",
    )
    webcache: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable web cache."
    )
    webcache_https: StatusEnum = Field(
        alias="webcache-https",
        default=StatusEnum.DISABLE,
        description="Enable/disable web cache for HTTPS.",
    )

    webproxy_forward_server: list[str] = Field(
        ...,
        alias="webproxy-forward-server",
        description="Webproxy forward server name.",
    )
    webproxy_profile: list[str] = Field(
        ..., alias="webproxy-profile", description="Webproxy profile name."
    )
    ztna_device_ownership: StatusEnum = Field(
        alias="ztna-device-ownership",
        default=StatusEnum.DISABLE,
        description="Enable/disable zero trust device ownership.",
    )
    ztna_ems_tag: list[str] = Field(
        ..., alias="ztna-ems-tag", description="Source ztna-ems-tag names."
    )

    ztna_geo_tag: list[str] = Field(
        ..., alias="ztna-geo-tag", description="Source ztna-geo-tag names."
    )
    ztna_policy_redirect: StatusEnum = Field(
        alias="ztna-policy-redirect",
        default=StatusEnum.DISABLE,
        description="Redirect ZTNA traffic to matching Access-Proxy proxy-policy.",
    )
    ztna_status: StatusEnum = Field(
        alias="ztna-status",
        default=StatusEnum.DISABLE,
        description="Enable/disable zero trust access.",
    )
    ztna_tags_match_logic: ZtnaTagsMatchLogicEnum = Field(
        alias="ztna-tags-match-logic",
        default=ZtnaTagsMatchLogicEnum.OR,
        description="ZTNA tag matching logic.",
    )


class PolicyRule(BaseModel):
    """
    Configure NGFW IPv4/IPv6 application policies.
    """

    name: str = Field(..., description="Policy name.", max_length=35)
    status: StatusEnum = Field(
        default=StatusEnum.ENABLE, description="Enable or disable this policy."
    )
    comments: str | None = Field(default=None, description="Comment.", max_length=1023)
    srcintf: list[str] = Field(default=[], description="Incoming (ingress) interface.")
    dstintf: list[str] = Field(default=[], description="Outgoing (egress) interface.")
    srcaddr: list[str] = Field(
        default=[], description="Source IPv4 address name and address group names."
    )
    srcaddr6: list[str] = Field(
        default=[], description="Source IPv6 address name and address group names."
    )
    dstaddr: list[str] = Field(
        default=[], description="Destination IPv4 address name and address group names."
    )
    dstaddr6: list[str] = Field(
        default=[], description="Destination IPv6 address name and address group names."
    )
    service: list[str] = Field(
        default=[], description="Service and service group names."
    )
    service_negate: StatusEnum = Field(
        alias="service-negate",
        default=StatusEnum.DISABLE,
        description="When enabled service specifies what the service must NOT be.",
    )
    srcaddr_negate: StatusEnum = Field(
        alias="srcaddr-negate",
        default=StatusEnum.DISABLE,
        description="When enabled srcaddr specifies what the source address"
        " must NOT be.",
    )
    schedule: list[str] = Field(default=["always"], description="Schedule name.")
    logtraffic: LogtrafficEnum = Field(
        default=LogtrafficEnum.UTM,
        description="Enable or disable logging. Log all sessions or security"
        " profile sessions.",
    )


class FortiManagerFirewallPolicyV1(PolicyRule):
    """
    Fortimanager firewall policy v1
    """

    action: ActionEnum = Field(
        default=ActionEnum.DENY, description="Policy action (accept/deny/ipsec)."
    )
