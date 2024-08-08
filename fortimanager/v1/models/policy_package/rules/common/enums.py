"""
policy package common model
"""

from enum import Enum


class ActionEnum(Enum):
    """
    rule action
    """

    ACCEPT = "accept"  # 1
    DENY = "deny"  # 0
    IPSEC = "ipsec"  # 2


class StatusEnum(Enum):
    """
    eanble / disable a feature
    """

    DISABLE = "disable"  # 0
    ENABLE = "enable"  # 1


class FirewallSessionDirtyEnum(Enum):
    """
    check option
    """

    CHECK_ALL = "check-all"  # 0
    CHECK_NEW = "check-new"  # 1


class GeoipMatchEnum(Enum):
    """
    geo location type
    """

    PHYSICAL_LOCATION = "physical-location"  # 0
    REGISTERED_LOCATION = "registered-location"  # 1


class InspectionModeEnum(Enum):
    """
    inspection mode
    """

    FLOW = "flow"  # 1
    PROXY = "proxy"  # 0


class LogtrafficEnum(Enum):
    """
    log traffic mode
    """

    ALL = "all"  # 2
    DISABLE = "disable"  # 0
    UTM = "utm"  # 3


class ProfileTypeEnum(Enum):
    """
    profile type
    """

    GROUP = "group"  # 1
    SINGLE = "single"  # 0


class ReputationDirectionEnum(Enum):
    """
    direction of the initial traffic for reputation
    """

    DESTINATION = "destination"  # 2
    SOURCE = "source"  # 1


class TcpSessionWithoutSynEnum(Enum):
    """
    tcp session without syn
    """

    ALL = "all"  # 0
    DATA_ONLY = "data-only"  # 1
    DISABLE = "disable"  # 2


class WanoptDetectionEnum(Enum):
    """
    WAN optimization auto-detection mode
    """

    ACTIVE = "active"  # 1
    OFF = "off"  # 3
    PASSIVE = "passive"  # 2


class WanoptPassiveOptEnum(Enum):
    """
    WAN optimization passive mode options
    """

    DEFAULT = "default"  # 0
    NON_TRANSPARENT = "non-transparent"  # 2
    TRANSPARENT = "transparent"  # 1


class ZtnaTagsMatchLogicEnum(Enum):
    """
    ZTNA tag matching logic
    """

    AND = "and"  # 1
    OR = "or"  # 0


# Virtual IP


class SslClientRenegotiationEnum(Enum):
    """
    ssl client renegotiation enum
    """

    ALLOW = "allow"  # 1
    DENY = "deny"  # 0
    SECURE = "secure"  # 14


class HealthcheckEnum(Enum):
    """
    check the responsiveness of the real server before forwarding traffic
    """

    DISABLE = "disable"  # 0
    ENABLE = "enable"  # 1
    VIP = "vip"  # 3


class SslDhBitsEnum(Enum):
    """
    ssldh bits enum
    """

    B1024 = "1024"  # 1
    B1536 = "1536"  # 2
    B2048 = "2048"  # 3
    B3072 = "3072"  # 4
    B4096 = "4096"  # 5
    B768 = "768"  # 0


class SslHpkpEnum(Enum):
    """
    ssl hpkp enum
    """

    DISABLE = "disable"  # 0
    ENABLE = "enable"  # 1
    REPORT_ONLY = "report-only"  # 2


class CipherEnum(Enum):
    """
    Cipher suite names
    """

    TLS_AES_128_GCM_SHA256 = "TLS-AES-128-GCM-SHA256"  # 68
    TLS_AES_256_GCM_SHA384 = "TLS-AES-256-GCM-SHA384"  # 69
    TLS_CHACHA20_POLY1305_SHA256 = "TLS-CHACHA20-POLY1305-SHA256"  # 70
    TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA = "TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA"  # 66
    TLS_DHE_DSS_WITH_AES_128_CBC_SHA = "TLS-DHE-DSS-WITH-AES-128-CBC-SHA"  # 38
    TLS_DHE_DSS_WITH_AES_128_CBC_SHA256 = "TLS-DHE-DSS-WITH-AES-128-CBC-SHA256"  # 40
    TLS_DHE_DSS_WITH_AES_128_GCM_SHA256 = "TLS-DHE-DSS-WITH-AES-128-GCM-SHA256"  # 41
    TLS_DHE_DSS_WITH_AES_256_CBC_SHA = "TLS-DHE-DSS-WITH-AES-256-CBC-SHA"  # 39
    TLS_DHE_DSS_WITH_AES_256_CBC_SHA256 = "TLS-DHE-DSS-WITH-AES-256-CBC-SHA256"  # 42
    TLS_DHE_DSS_WITH_AES_256_GCM_SHA384 = "TLS-DHE-DSS-WITH-AES-256-GCM-SHA384"  # 43
    TLS_DHE_DSS_WITH_ARIA_128_CBC_SHA256 = "TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256"  # 60
    TLS_DHE_DSS_WITH_ARIA_256_CBC_SHA384 = "TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384"  # 61
    TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA = (
        "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA"  # 55
    )
    TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA256 = (
        "TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256"  # 57
    )
    TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA = (
        "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA"  # 56
    )
    TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA256 = (
        "TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256"  # 58
    )
    TLS_DHE_DSS_WITH_DES_CBC_SHA = "TLS-DHE-DSS-WITH-DES-CBC-SHA"  # 67
    TLS_DHE_DSS_WITH_SEED_CBC_SHA = "TLS-DHE-DSS-WITH-SEED-CBC-SHA"  # 59
    TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA = "TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA"  # 17
    TLS_DHE_RSA_WITH_AES_128_CBC_SHA = "TLS-DHE-RSA-WITH-AES-128-CBC-SHA"  # 18
    TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 = "TLS-DHE-RSA-WITH-AES-128-CBC-SHA256"  # 20
    TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 = "TLS-DHE-RSA-WITH-AES-128-GCM-SHA256"  # 36
    TLS_DHE_RSA_WITH_AES_256_CBC_SHA = "TLS-DHE-RSA-WITH-AES-256-CBC-SHA"  # 19
    TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 = "TLS-DHE-RSA-WITH-AES-256-CBC-SHA256"  # 21
    TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 = "TLS-DHE-RSA-WITH-AES-256-GCM-SHA384"  # 37
    TLS_DHE_RSA_WITH_ARIA_128_CBC_SHA256 = "TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256"  # 27
    TLS_DHE_RSA_WITH_ARIA_256_CBC_SHA384 = "TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384"  # 28
    TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA = (
        "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA"  # 22
    )
    TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 = (
        "TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256"  # 24
    )
    TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA = (
        "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA"  # 23
    )
    TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA256 = (
        "TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256"  # 25
    )
    TLS_DHE_RSA_WITH_CHACHA20_POLY1305_SHA256 = (
        "TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256"  # 35
    )
    TLS_DHE_RSA_WITH_DES_CBC_SHA = "TLS-DHE-RSA-WITH-DES-CBC-SHA"  # 16
    TLS_DHE_RSA_WITH_SEED_CBC_SHA = "TLS-DHE-RSA-WITH-SEED-CBC-SHA"  # 26
    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA = "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA"  # 48
    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 = (
        "TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256"  # 49
    )
    TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 = (
        "TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256"  # 50
    )
    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA = "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA"  # 71
    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 = (
        "TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384"  # 51
    )
    TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 = (
        "TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384"  # 52
    )
    TLS_ECDHE_ECDSA_WITH_ARIA_128_CBC_SHA256 = (
        "TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256"  # 64
    )
    TLS_ECDHE_ECDSA_WITH_ARIA_256_CBC_SHA384 = (
        "TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384"  # 65
    )
    TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 = (
        "TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256"  # 34
    )
    TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA = "TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA"  # 30
    TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA = "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA"  # 31
    TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 = (
        "TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256"  # 44
    )
    TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 = (
        "TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"  # 45
    )
    TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA = "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA"  # 32
    TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 = (
        "TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384"  # 46
    )
    TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 = (
        "TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384"  # 47
    )
    TLS_ECDHE_RSA_WITH_ARIA_128_CBC_SHA256 = (
        "TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256"  # 62
    )
    TLS_ECDHE_RSA_WITH_ARIA_256_CBC_SHA384 = (
        "TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384"  # 63
    )
    TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 = (
        "TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256"  # 33
    )
    TLS_ECDHE_RSA_WITH_RC4_128_SHA = "TLS-ECDHE-RSA-WITH-RC4-128-SHA"  # 29
    TLS_RSA_WITH_3DES_EDE_CBC_SHA = "TLS-RSA-WITH-3DES-EDE-CBC-SHA"  # 4
    TLS_RSA_WITH_AES_128_CBC_SHA = "TLS-RSA-WITH-AES-128-CBC-SHA"  # 5
    TLS_RSA_WITH_AES_128_CBC_SHA256 = "TLS-RSA-WITH-AES-128-CBC-SHA256"  # 7
    TLS_RSA_WITH_AES_128_GCM_SHA256 = "TLS-RSA-WITH-AES-128-GCM-SHA256"  # 53
    TLS_RSA_WITH_AES_256_CBC_SHA = "TLS-RSA-WITH-AES-256-CBC-SHA"  # 6
    TLS_RSA_WITH_AES_256_CBC_SHA256 = "TLS-RSA-WITH-AES-256-CBC-SHA256"  # 8
    TLS_RSA_WITH_AES_256_GCM_SHA384 = "TLS-RSA-WITH-AES-256-GCM-SHA384"  # 54
    TLS_RSA_WITH_ARIA_128_CBC_SHA256 = "TLS-RSA-WITH-ARIA-128-CBC-SHA256"  # 14
    TLS_RSA_WITH_ARIA_256_CBC_SHA384 = "TLS-RSA-WITH-ARIA-256-CBC-SHA384"  # 15
    TLS_RSA_WITH_CAMELLIA_128_CBC_SHA = "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA"  # 9
    TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256 = "TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256"  # 11
    TLS_RSA_WITH_CAMELLIA_256_CBC_SHA = "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA"  # 10
    TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256 = "TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256"  # 12
    TLS_RSA_WITH_DES_CBC_SHA = "TLS-RSA-WITH-DES-CBC-SHA"  # 3
    TLS_RSA_WITH_RC4_128_MD5 = "TLS-RSA-WITH-RC4-128-MD5"  # 1
    TLS_RSA_WITH_RC4_128_SHA = "TLS-RSA-WITH-RC4-128-SHA"  # 2
    TLS_RSA_WITH_SEED_CBC_SHA = "TLS-RSA-WITH-SEED-CBC-SHA"  # 13


class SslServerVersionEnum(Enum):
    """
    SSL/TLS version + client
    """

    CLIENT = "client"  # 16
    SSL_3_0 = "ssl-3.0"  # 1
    TLS_1_0 = "tls-1.0"  # 2
    TLS_1_1 = "tls-1.1"  # 4
    TLS_1_2 = "tls-1.2"  # 8
    TLS_1_3 = "tls-1.3"  # 32


class HttpCookieShareEnum(Enum):
    """
    sharing of cookies mode
    """

    DISABLE = "disable"  # 0
    SAME_IP = "same-ip"  # 1


class LdbMethodEnum(Enum):
    """
    distribution sessions mode
    """

    FIRST_ALIVE = "first-alive"  # 5
    HTTP_HOST = "http-host"  # 6
    LEAST_RTT = "least-rtt"  # 4
    LEAST_SESSION = "least-session"  # 3
    ROUND_ROBIN = "round-robin"  # 1
    STATIC = "static"  # 0
    WEIGHTED = "weighted"  # 2


class PersistenceEnum(Enum):
    """
    persistence mode
    """

    HTTP_COOKIE = "http-cookie"  # 3
    NONE = "none"  # 1
    SSL_SESSION_ID = "ssl-session-id"  # 4


class ServerTypeEnum(Enum):
    """
    server types
    """

    HTTP = "http"  # 1
    HTTPS = "https"  # 2
    IMAPS = "imaps"  # 7
    IP = "ip"  # 6
    POP3S = "pop3s"  # 8
    SMTPS = "smtps"  # 9
    SSL = "ssl"  # 3
    TCP = "tcp"  # 4
    UDP = "udp"  # 5


class SslAlgorithmEnum(Enum):
    """
    ssl Algorithms
    """

    CUSTOM = "custom"  # 4
    HIGH = "high"  # 1
    LOW = "low"  # 3
    MEDIUM = "medium"  # 2


class SslModeEnum(Enum):
    """
    ssl mode
    """

    FULL = "full"  # 2
    HALF = "half"  # 1


class SessionStateTypeEnum(Enum):
    """
    session state type
    """

    BOTH = "both"  # 3
    COUNT = "count"  # 2
    DISABLE = "disable"  # 0
    TIME = "time"  # 1


class SslPfsEnum(Enum):
    """
    cipher suites
    """

    ALLOW = "allow"  # 2
    DENY = "deny"  # 1
    REQUIRE = "require"  # 0


class SslServerAlgorithmEnum(Enum):
    """
    ssl Algorithms + client
    """

    CLIENT = "client"  # 6
    CUSTOM = "custom"  # 5
    HIGH = "high"  # 1
    LOW = "low"  # 2
    MEDIUM = "medium"  # 4
