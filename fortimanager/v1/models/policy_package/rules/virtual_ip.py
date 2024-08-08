"""
Fortimanager virtual IP rule model
"""

# pylint: disable=line-too-long, too-many-lines
from enum import Enum

from pydantic import BaseModel, Field

from common.southbound.fortimanager.v1.models.policy_package.rules.common.enums import (
    CipherEnum,
    HealthcheckEnum,
    HttpCookieShareEnum,
    LdbMethodEnum,
    PersistenceEnum,
    ServerTypeEnum,
    SessionStateTypeEnum,
    SslAlgorithmEnum,
    SslClientRenegotiationEnum,
    SslDhBitsEnum,
    SslHpkpEnum,
    SslModeEnum,
    SslPfsEnum,
    SslServerAlgorithmEnum,
    SslServerVersionEnum,
    StatusEnum,
)


class TypeEnum(Enum):
    """
    Encryption type
    """

    ADDRESS = "address"  # 2
    IP = "ip"  # 1
    SSL_3_0 = "ssl-3.0"  # 1
    TLS_1_0 = "tls-1.0"  # 2
    TLS_1_1 = "tls-1.1"  # 4
    TLS_1_2 = "tls-1.2"  # 8
    TLS_1_3 = "tls-1.3"  # 32


class PortmappingTypeEnum(Enum):
    """
    Port mapping type
    """

    MAP_1_TO_1 = "1-to-1"  # 0
    MAP_M_TO_N = "m-to-n"  # 1


class ProtocolEnum(Enum):
    """
    Protocol types
    """

    ICMP = "icmp"  # 4
    SCTP = "sctp"  # 3
    TCP = "tcp"  # 1
    UDP = "udp"  # 2


class DMTypeEnum(Enum):
    """
    DM type Enum
    """

    ACCESS_PROXY = "access-proxy"  # 6
    DNS_TRANSLATION = "dns-translation"  # 4
    FQDN = "fqdn"  # 5
    LOAD_BALANCE = "load-balance"  # 1
    SERVER_LOAD_BALANCE = "server-load-balance"  # 3
    STATIC_NAT = "static-nat"  # 0


class RSStatusEnum(Enum):
    """
    real server status
    """

    ACTIVE = "active"  # 0
    DISABLE = "disable"  # 2
    STANDBY = "standby"  # 1


class VersionsEnum(Enum):
    """
    SSL/TLS versions
    """

    SSL_3_0 = "ssl-3.0"  # 1
    TLS_1_0 = "tls-1.0"  # 2
    TLS_1_1 = "tls-1.1"  # 4
    TLS_1_2 = "tls-1.2"  # 8
    TLS_1_3 = "tls-1.3"  # 32


class DynamicMapping(BaseModel):
    """
    Common properties
    """

    color: int = Field(
        default=0,
        description="Color of icon on the GUI.",
        le=32,
    )
    comment: str = Field(
        ...,
        description="Comment.",
        max_length=255,
    )

    h2_support: StatusEnum = Field(
        alias="h2-support",
        default=StatusEnum.ENABLE,
        description="Enable/disable HTTP2 support (default = enable).",
    )
    h3_support: StatusEnum = Field(
        alias="h3-support",
        default=StatusEnum.DISABLE,
        description="Enable/disable HTTP3/QUIC support (default = disable).",
    )
    http_cookie_age: int = Field(
        alias="http-cookie-age",
        default=60,
        description="Time in minutes that client web browsers should keep a "
        "cookie. Default is 60 minutes. 0 = no time limit.",
        le=525600,
    )
    http_cookie_domain: str = Field(
        ...,
        alias="http-cookie-domain",
        description="Domain that HTTP cookie persistence should apply to.",
        max_length=35,
    )
    http_cookie_domain_from_host: StatusEnum = Field(
        alias="http-cookie-domain-from-host",
        default=StatusEnum.DISABLE,
        description="Enable/disable use of HTTP cookie domain from host field in HTTP.",
    )
    http_cookie_generation: int = Field(
        alias="http-cookie-generation",
        default=0,
        description="Generation of HTTP cookie to be accepted. Changing "
        "invalidates all existing cookies.",
        le=4294967295,
    )
    http_cookie_path: str = Field(
        ...,
        alias="http-cookie-path",
        description="Limit HTTP cookie persistence to the specified path.",
        max_length=35,
    )
    http_cookie_share: HttpCookieShareEnum = Field(
        alias="http-cookie-share",
        default=HttpCookieShareEnum.SAME_IP,
        description="Control sharing of cookies across virtual servers. Use "
        "of same-ip means a cookie from one virtual server can be used by "
        "another. Disable stops cookie sharing.",
    )
    http_ip_header: StatusEnum = Field(
        alias="http-ip-header",
        default=StatusEnum.DISABLE,
        description="For HTTP multiplexing, enable to add the original client "
        "IP address in the XForwarded-For HTTP header.",
    )
    http_ip_header_name: str = Field(
        ...,
        alias="http-ip-header-name",
        description="For HTTP multiplexing, enter a custom HTTPS"
        " header name. The original client IP address is added to"
        " this header. If empty, X-Forwarded-For is used.",
        max_length=35,
    )
    http_multiplex: StatusEnum = Field(
        alias="http-multiplex",
        default=StatusEnum.DISABLE,
        description="Enable/disable HTTP multiplexing.",
    )

    http_redirect: StatusEnum = Field(
        alias="http-redirect",
        default=StatusEnum.DISABLE,
        description="Enable/disable redirection of HTTP to HTTPS.",
    )
    https_cookie_secure: StatusEnum = Field(
        alias="https-cookie-secure",
        default=StatusEnum.DISABLE,
        description="Enable/disable verification that inserted HTTPS"
        " cookies are secure.",
    )
    id: int = Field(
        default=0,
        description="Custom defined ID.",
        le=65535,
    )

    ldb_method: LdbMethodEnum = Field(
        alias="ldb-method",
        default=LdbMethodEnum.STATIC,
        description="Method used to distribute sessions to real servers.",
    )
    mappedport: str = Field(
        default="0",
        description="Port number range on the destination network to which"
        " the external port number range is mapped.",
    )
    max_embryonic_connections: int = Field(
        alias="max-embryonic-connections",
        default=1000,
        description="Maximum number of incomplete connections.",
        le=100000,
    )
    monitor: list[str] = Field(
        ...,
        description="Name of the health check monitor to use when polling to "
        "determine a virtual server's connectivity status.",
    )

    nat_source_vip: StatusEnum = Field(
        alias="nat-source-vip",
        default=StatusEnum.DISABLE,
        description="Enable/disable forcing the source NAT mapped IP to the "
        "external IP for all traffic.",
    )

    outlook_web_access: StatusEnum = Field(
        alias="outlook-web-access",
        default=StatusEnum.DISABLE,
        description="Enable to add the Front-End-Https header for Microsoft "
        "Outlook Web Access.",
    )
    persistence: PersistenceEnum = Field(
        default=PersistenceEnum.NONE,
        description="Configure how to make sure that clients connect to the same "
        "server every time they make a request that is part of the same session.",
    )
    portforward: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable port forwarding."
    )

    protocol: ProtocolEnum = Field(
        default=ProtocolEnum.TCP, description="Protocol to use when forwarding packets."
    )
    server_type: ServerTypeEnum = Field(
        ...,
        alias="server-type",
        description="Protocol to be load balanced by the virtual server"
        " (also called the server load balance virtual IP).",
    )

    ssl_accept_ffdhe_groups: StatusEnum = Field(
        alias="ssl-accept-ffdhe-groups",
        default=StatusEnum.ENABLE,
        description="Enable/disable FFDHE cipher suite for SSL key exchange.",
    )
    ssl_algorithm: SslAlgorithmEnum = Field(
        ...,
        alias="ssl-algorithm",
        description="Permitted encryption algorithms for SSL sessions according"
        " to encryption strength.",
    )
    ssl_certificate: list[str] = Field(
        ...,
        alias="ssl-certificate",
        description="Name of the certificate to use for SSL handshake.",
    )
    ssl_client_fallback: StatusEnum = Field(
        alias="ssl-client-fallback",
        default=StatusEnum.ENABLE,
        description="Enable/disable support for preventing Downgrade Attacks on"
        " client connections (RFC 7507).",
    )
    ssl_client_rekey_count: int = Field(
        alias="ssl-client-rekey-count",
        default=0,
        description="Maximum length of data in MB before triggering a client "
        "rekey (0 = disable).",
        le=1048576,
        ge=200,
    )
    ssl_client_renegotiation: SslClientRenegotiationEnum = Field(
        alias="ssl-client-renegotiation",
        default=SslClientRenegotiationEnum.SECURE,
        description="Allow, deny, or require secure renegotiation of client sessions"
        " to comply with RFC 5746.",
    )
    ssl_client_session_state_max: int = Field(
        alias="ssl-client-session-state-max",
        default=1000,
        description="Maximum number of client to FortiGate SSL session states to keep.",
        le=10000,
        ge=1,
    )
    ssl_client_session_state_timeout: int = Field(
        alias="ssl-client-session-state-timeout",
        default=30,
        description="Number of minutes to keep client to FortiGate SSL session state.",
        le=14400,
        ge=1,
    )
    ssl_client_session_state_type: SessionStateTypeEnum = Field(
        alias="ssl-client-session-state-type",
        default=SessionStateTypeEnum.BOTH,
        description="How to expire SSL sessions for the segment of the SSL connection"
        " between the client and the FortiGate.",
    )
    ssl_dh_bits: SslDhBitsEnum = Field(
        alias="ssl-dh-bits",
        default=SslDhBitsEnum.B2048,
        description="Number of bits to use in the Diffie-Hellman exchange for RSA"
        " encryption of SSL sessions.",
    )
    ssl_hpkp: SslHpkpEnum = Field(
        alias="ssl-hpkp",
        default=SslHpkpEnum.DISABLE,
        description="Enable/disable including HPKP header in response.",
    )
    ssl_hpkp_age: int = Field(
        alias="ssl-hpkp-age",
        default=5184000,
        description="Number of seconds the client should honor the HPKP setting.",
        le=157680000,
        ge=60,
    )
    ssl_hpkp_backup: list[str] = Field(
        ...,
        alias="ssl-hpkp-backup",
        description="Certificate to generate backup HPKP pin from.",
    )
    ssl_hpkp_include_subdomains: StatusEnum = Field(
        alias="ssl-hpkp-include-subdomains",
        default=StatusEnum.DISABLE,
        description="Indicate that HPKP header applies to all subdomains.",
    )
    ssl_hpkp_primary: list[str] = Field(
        ...,
        alias="ssl-hpkp-primary",
        description="Certificate to generate primary HPKP pin from.",
    )
    ssl_hpkp_report_uri: str = Field(
        ...,
        alias="ssl-hpkp-report-uri",
        description="URL to report HPKP violations to.",
        max_length=255,
    )
    ssl_hsts: StatusEnum = Field(
        alias="ssl-hsts",
        default=StatusEnum.DISABLE,
        description="Enable/disable including HSTS header in response.",
    )
    ssl_hsts_age: int = Field(
        alias="ssl-hsts-age",
        default=5184000,
        description="Number of seconds the client should honor the HSTS setting.",
        le=157680000,
        ge=60,
    )
    ssl_hsts_include_subdomains: StatusEnum = Field(
        alias="ssl-hsts-include-subdomains",
        default=StatusEnum.DISABLE,
        description="Indicate that HSTS header applies to all subdomains.",
    )
    ssl_http_location_conversion: StatusEnum = Field(
        alias="ssl-http-location-conversion",
        default=StatusEnum.DISABLE,
        description="Enable to replace HTTP with HTTPS in the reply's Location HTTP"
        " header field.",
    )
    ssl_http_match_host: StatusEnum = Field(
        alias="ssl-http-match-host",
        default=StatusEnum.ENABLE,
        description="Enable/disable HTTP host matching for location conversion.",
    )
    ssl_max_version: VersionsEnum = Field(
        ...,
        alias="ssl-max-version",
        description="Highest SSL/TLS version acceptable from a client.",
    )
    ssl_min_version: VersionsEnum = Field(
        ...,
        alias="ssl-min-version",
        description="Lowest SSL/TLS version acceptable from a client.",
    )
    ssl_mode: SslModeEnum = Field(
        alias="ssl-mode",
        default=SslModeEnum.HALF,
        description="Apply SSL offloading between the client and the FortiGate"
        " (half) or from the client to the FortiGate and from the FortiGate"
        " to the server (full).",
    )
    ssl_pfs: SslPfsEnum = Field(
        alias="ssl-pfs",
        default=SslPfsEnum.REQUIRE,
        description="Select the cipher suites that can be used for SSL perfect "
        "forward secrecy (PFS). Applies to both client and server sessions.",
    )
    ssl_send_empty_frags: StatusEnum = Field(
        alias="ssl-send-empty-frags",
        default=StatusEnum.ENABLE,
        description="Enable/disable sending empty fragments to avoid CBC IV attacks"
        " (SSL 3.0 & TLS 1.0 only). May need to be disabled for compatibility "
        "with older systems.",
    )
    ssl_server_algorithm: SslServerAlgorithmEnum = Field(
        alias="ssl-server-algorithm",
        default=SslServerAlgorithmEnum.CLIENT,
        description="Permitted encryption algorithms for the server side of SSL full"
        " mode sessions according to encryption strength.",
    )
    ssl_server_max_version: SslServerVersionEnum = Field(
        alias="ssl-server-max-version",
        default=SslServerVersionEnum.CLIENT,
        description="Highest SSL/TLS version acceptable from a server. Use the client"
        " setting by default.",
    )
    ssl_server_min_version: SslServerVersionEnum = Field(
        alias="ssl-server-min-version",
        default=SslServerVersionEnum.CLIENT,
        description="Lowest SSL/TLS version acceptable from a server. Use the client"
        " setting by default.",
    )
    ssl_server_renegotiation: StatusEnum = Field(
        alias="ssl-server-renegotiation",
        default=StatusEnum.ENABLE,
        description="Enable/disable secure renegotiation to comply with RFC 5746.",
    )
    ssl_server_session_state_max: int = Field(
        alias="ssl-server-session-state-max",
        default=100,
        description="Maximum number of FortiGate to Server SSL session states to keep.",
        le=10000,
        ge=1,
    )
    ssl_server_session_state_timeout: int = Field(
        alias="ssl-server-session-state-timeout",
        default=60,
        description="Number of minutes to keep FortiGate to Server SSL session state.",
        le=14400,
        ge=1,
    )
    ssl_server_session_state_type: SessionStateTypeEnum = Field(
        alias="ssl-server-session-state-type",
        default=SessionStateTypeEnum.BOTH,
        description="How to expire SSL sessions for the segment of the SSL connection"
        " between the server and the FortiGate.",
    )

    uuid: str = Field(
        default="00000000-0000-0000-0000-000000000000",
        description="Universally Unique Identifier (UUID; automatically assigned but "
        "can be manually reset).",
    )
    weblogic_server: StatusEnum = Field(
        alias="weblogic-server",
        default=StatusEnum.DISABLE,
        description="Enable to add an HTTP header to indicate SSL offloading for "
        "a WebLogic server.",
    )
    websphere_server: StatusEnum = Field(
        alias="websphere-server",
        default=StatusEnum.DISABLE,
        description="Enable to add an HTTP header to indicate SSL offloading for a "
        "WebSphere server.",
    )


class GslbPublicIps(BaseModel):
    """
    Publicly accessible IP addresses for the FortiGSLB service.
    """

    index: int = Field(
        default=0, description="Index of this public IP setting.", le=4294967295
    )
    ip: str = Field(
        default="0.0.0.0",  # noqa: S104
        description="The publicly accessible IP address.",
    )


class Quic(BaseModel):
    """
    QUIC setting.
    """

    ack_delay_exponent: int = Field(
        alias="ack-delay-exponent",
        default=3,
        description="ACK delay exponent (1 - 20, default = 3).",
        le=20,
        ge=1,
    )
    active_connection_id_limit: int = Field(
        alias="active-connection-id-limit",
        default=2,
        description="Active connection ID limit (1 - 8, default = 2).",
        le=8,
        ge=1,
    )
    active_migration: StatusEnum = Field(
        alias="active-migration",
        default=StatusEnum.DISABLE,
        description="Enable/disable active migration (default = disable).",
    )
    grease_quic_bit: StatusEnum = Field(
        alias="grease-quic-bit",
        default=StatusEnum.ENABLE,
        description="Enable/disable grease QUIC bit (default = enable).",
    )
    max_ack_delay: int = Field(
        alias="max-ack-delay",
        default=25,
        description="Maximum ACK delay in milliseconds (1 - 16383, default = 25).",
        le=16383,
        ge=1,
    )
    max_datagram_frame_size: int = Field(
        alias="max-datagram-frame-size",
        default=1500,
        description="Maximum datagram frame size in bytes (1 - 1500, default = 1500).",
        le=1500,
        ge=1,
    )
    max_idle_timeout: int = Field(
        alias="max-idle-timeout",
        default=30000,
        description="Maximum idle timeout milliseconds (1 - 60000, default = 30000).",
        le=60000,
        ge=1,
    )
    max_udp_payload_size: int = Field(
        alias="max-udp-payload-size",
        default=1500,
        description="Maximum UDP payload size in bytes (1200 - 1500, default = 1500).",
        le=1500,
        ge=1200,
    )


class Realservers(BaseModel):
    """
    Select the real servers that this server load balancing VIP will distribute
    traffic to.
    """

    address: list[str] | None = Field(
        ..., description="Dynamic address of the real server."
    )
    client_ip: list[str] | str = Field(
        alias="client-ip",
        default="0.0.0.0",  # noqa: S104
        description="Only clients in this IP range can connect to this real server.",
    )
    healthcheck: HealthcheckEnum = Field(
        default=HealthcheckEnum.VIP,
        description="Enable to check the responsiveness of the real server before"
        " forwarding traffic.",
    )
    holddown_interval: int = Field(
        alias="holddown-interval",
        default=300,
        description="Time in seconds that the health check monitor continues"
        " to monitor and unresponsive server that should be active.",
        le=65535,
        ge=30,
    )
    http_host: str = Field(
        ...,
        alias="http-host",
        description="HTTP server domain name in HTTP header.",
        max_length=63,
    )
    id: int = Field(default=0, description="Real server ID.", le=4294967295)
    ip: str = Field(default="::", description="IP address of the real server.")
    max_connections: int = Field(
        alias="max-connections",
        default=0,
        description="Max number of active connections that can be directed to the "
        "real server. When reached, sessions are sent to other real servers.",
        le=2147483647,
    )
    monitor: list[str] = Field(
        ...,
        description="Name of the health check monitor to use when polling to "
        "determine a virtual server's connectivity status.",
    )
    port: int = Field(
        default=0,
        description="Port for communicating with the real server. Required if port"
        " forwarding is enabled.",
        le=65535,
        ge=1,
    )
    status: RSStatusEnum = Field(
        default=RSStatusEnum.ACTIVE,
        description="Set the status of the real server to active so that it can accept"
        " traffic, or on standby or disabled so no traffic is sent.",
    )
    translate_host: StatusEnum = Field(
        alias="translate-host",
        default=StatusEnum.ENABLE,
        description="Enable/disable translation of hostname/IP from virtual server "
        "to real server.",
    )
    type: TypeEnum | None = Field(default=TypeEnum.IP, description="Type of address.")
    weight: int = Field(
        default=1,
        description="Weight of the real server. If weighted load balancing is enabled,"
        " the server with the highest weight gets more connections.",
        le=255,
        ge=1,
    )


class SslCipherSuites(BaseModel):
    """
    SSL/TLS cipher suites acceptable from a client, ordered by priority.
    """

    cipher: CipherEnum = Field(..., description="Cipher suite name.")
    priority: int = Field(
        default=0, description="SSL/TLS cipher suites priority.", le=4294967295
    )
    versions: VersionsEnum = Field(
        ..., description="SSL/TLS versions that the cipher suite can be used with."
    )


class PolicyPackageFirewall(BaseModel):
    """
    Main policy package firewall model
    """

    dynamic_mapping: list[DynamicMapping] | None = Field(default=None)

    quic: Quic | None = Field(default=None, description="QUIC setting.")

    realservers: list[Realservers] | None = Field(
        default=None,
        description="Select the real servers that this server load balancing VIP"
        " will distribute traffic to.",
    )
    ssl_cipher_suites: list[SslCipherSuites] | None = Field(
        alias="ssl-cipher-suites",
        default=None,
        description="SSL/TLS cipher suites acceptable from a client, ordered "
        "by priority.",
    )
    ssl_server_cipher_suites: list[SslCipherSuites] | None = Field(
        alias="ssl-server-cipher-suites",
        default=None,
        description="SSL/TLS cipher suites to offer to a server, ordered by priority.",
    )


class FirewallVip(PolicyPackageFirewall, DynamicMapping):
    """
    Configure virtual IP for IPv4.
    """

    add_nat46_route: StatusEnum = Field(
        alias="add-nat46-route",
        default=StatusEnum.ENABLE,
        description="Enable/disable adding NAT46 route.",
    )

    arp_reply: StatusEnum = Field(
        alias="arp-reply",
        default=StatusEnum.ENABLE,
        description="Enable to respond to ARP requests for this virtual IP address."
        " Enabled by default.",
    )

    gslb_public_ips: list[GslbPublicIps] | None = Field(
        alias="gslb-public-ips",
        default=None,
        description="Publicly accessible IP addresses for the FortiGSLB service.",
    )
    dns_mapping_ttl: int = Field(
        alias="dns-mapping-ttl",
        default=0,
        description="DNS mapping TTL (Set to zero to use TTL in DNS response, "
        "default = 0).",
        le=604800,
    )
    extaddr: list[str] = Field(..., description="External FQDN address name.")
    extintf: list[str] = Field(
        ...,
        description="Interface connected to the source network that receives the "
        "packets that will be forwarded to the destination network.",
    )
    extip: str = Field(
        default="0.0.0.0",  # noqa: S104
        description="IP address or address range on the external interface that you "
        "want to map to an address or address range on the destination network.",
    )
    extport: str = Field(
        default="0",
        description="Incoming port number range that you want to map to a port number"
        " range on the destination network.",
    )
    gratuitous_arp_interval: int = Field(
        alias="gratuitous-arp-interval",
        default=0,
        description="Enable to have the VIP send gratuitous ARPs. 0=disabled. Set"
        " from 5 up to 8640000 seconds to enable.",
        le=8640000,
        ge=5,
    )
    gslb_domain_name: str = Field(
        ...,
        alias="gslb-domain-name",
        description="Domain to use when integrating with FortiGSLB.",
        max_length=255,
    )
    gslb_hostname: str = Field(
        ...,
        alias="gslb-hostname",
        description="Hostname to use within the configured FortiGSLB domain.",
        max_length=35,
    )

    ipv6_mappedip: str = Field(
        alias="ipv6-mappedip",
        default="::",
        description="Range of mapped IPv6 addresses. Specify the start IPv6 address"
        "followed by a space and the end IPv6 address.",
    )
    ipv6_mappedport: str = Field(
        alias="ipv6-mappedport",
        default="0",
        description="IPv6 port number range on the destination network to which the "
        "external port number range is mapped.",
    )
    status: StatusEnum = Field(
        default=StatusEnum.ENABLE, description="Enable/disable VIP."
    )

    service: list[str] = Field(..., description="Service name.")
    src_filter: list[str] = Field(
        ...,
        alias="src-filter",
        description="Source address filter. Each address must be either an IP/subnet"
        " (x.x.x.x/n) or a range (x.x.x.x-y.y.y.y). Separate addresses with spaces.",
    )
    srcintf_filter: list[str] = Field(
        ...,
        alias="srcintf-filter",
        description="Interfaces to which the VIP applies. Separate the names "
        "with spaces.",
    )

    mapped_addr: list[str] = Field(
        ..., alias="mapped-addr", description="Mapped FQDN address name."
    )
    mappedip: list[str] = Field(
        ...,
        description="IP address or address range on the destination network to "
        "which the external IP address is mapped.",
    )
    name: str = Field(..., description="Virtual IP name.", max_length=79)

    nat44: StatusEnum = Field(
        default=StatusEnum.ENABLE, description="Enable/disable NAT44."
    )
    nat46: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable NAT46."
    )
    one_click_gslb_server: StatusEnum = Field(
        alias="one-click-gslb-server",
        default=StatusEnum.DISABLE,
        description="Enable/disable one click GSLB server integration with FortiGSLB.",
    )
    portmapping_type: PortmappingTypeEnum = Field(
        alias="portmapping-type",
        default=PortmappingTypeEnum.MAP_1_TO_1,
        description="Port mapping type.",
    )
    http_multiplex_max_concurrent_request: int = Field(
        alias="http-multiplex-max-concurrent-request",
        default=0,
        description="Maximum number of concurrent requests that a multiplex server "
        "can handle (default = unlimited).",
        le=2147483647,
    )
    http_multiplex_max_request: int = Field(
        alias="http-multiplex-max-request",
        default=0,
        description="Maximum number of requests that a multiplex server can handle "
        "before disconnecting sessions (default = unlimited).",
        le=2147483647,
    )
    http_multiplex_ttl: int = Field(
        alias="http-multiplex-ttl",
        default=15,
        description="Time-to-live for idle connections to servers.",
        le=2147483647,
    )
    type: DMTypeEnum = Field(
        default=DMTypeEnum.STATIC_NAT,
        description="Configure a static NAT, load balance, server load balance, "
        "access proxy, DNS translation, or FQDN VIP.",
    )


class FortiManagerFirewallVipV1(BaseModel):
    """
    Fortimanager firewall virtual ipv
    """

    name: str = Field(..., description="Virtual IP name.", max_length=79)
    comment: str | None = Field(
        default=None,
        description="Comment.",
        max_length=255,
    )
    type: DMTypeEnum = Field(
        default=DMTypeEnum.STATIC_NAT,
        description="Configure a static NAT, load balance, server load balance, "
        "access proxy, DNS translation, or FQDN VIP.",
    )
    status: StatusEnum = Field(
        default=StatusEnum.ENABLE, description="Enable/disable VIP."
    )
    extip: str = Field(
        default="0.0.0.0",  # noqa: S104
        description="IP address or address range on the external interface that you "
        "want to map to an address or address range on the destination network.",
    )
    extport: str = Field(
        default="0",
        description="Incoming port number range that you want to map to a port number"
        " range on the destination network.",
    )
    extintf: list[str] = Field(
        default=[],
        description="Interface connected to the source network that receives the "
        "packets that will be forwarded to the destination network.",
    )
    mappedip: list[str] = Field(
        default=[],
        description="IP address or address range on the destination network to "
        "which the external IP address is mapped.",
    )
    mappedport: str = Field(
        default="0",
        description="Port number range on the destination network to which"
        " the external port number range is mapped.",
    )
    portforward: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable port forwarding."
    )
    protocol: ProtocolEnum = Field(
        default=ProtocolEnum.TCP,
        description="Protocol to use when forwarding packets.",
    )
    portmapping_type: PortmappingTypeEnum = Field(
        alias="portmapping-type",
        default=PortmappingTypeEnum.MAP_1_TO_1,
        description="Port mapping type.",
    )
    arp_reply: StatusEnum = Field(
        alias="arp-reply",
        default=StatusEnum.ENABLE,
        description="Enable to respond to ARP requests for this virtual IP address."
        " Enabled by default.",
    )
