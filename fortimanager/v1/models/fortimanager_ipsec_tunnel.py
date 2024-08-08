"""
Fortimanager ipsec tunnel V1 model
"""

# pylint: disable=line-too-long, too-many-lines
from enum import Enum
from ipaddress import IPv4Address, IPv6Address

from pydantic import BaseModel, Field

DEFAULT_NETWORK = "0.0.0.0/0.0.0.0"


class StatusEnum(Enum):
    """
    Enum representing Status option.
    """

    DISABLE = "disable"  # 0
    ENABLE = "enable"  # 1


class AssignIpFromEnum(Enum):
    """
    Enum to specify the method for assigning IP addresses.
    """

    DHCP = "dhcp"  # 2
    NAME = "name"  # 4
    RANGE = "range"  # 0
    USRGRP = "usrgrp"  # 1


class AuthmethodEnum(Enum):
    """
    Enum for specifying the authentication method.
    """

    PSK = "psk"  # 1
    SIGNATURE = "signature"  # 3


class AutoDiscoveryCrossoverEnum(Enum):
    """
    Enum to allow or block auto-discovery crossover.
    """

    ALLOW = "allow"  # 57
    BLOCK = "block"  # 0


class AutoDiscoveryShortcutsEnum(Enum):
    """
    Enum to control deletion of child shortcuts when the parent tunnel goes down.
    """

    DEPENDENT = "dependent"  # 2
    INDEPENDENT = "independent"  # 1


class CertTrustStoreEnum(Enum):
    """
    Enum to specify the certificate trust store location.
    """

    EMS = "ems"  # 2
    LOCAL = "local"  # 1


class DnsModeEnum(Enum):
    """
    Enum to specify the DNS server mode.
    """

    AUTO = "auto"  # 0
    MANUAL = "manual"  # 1


class DpdEnum(Enum):
    """
    Enum for Dead Peer Detection (DPD) modes.
    """

    DISABLE = "disable"  # 0
    ON_DEMAND = "on-demand"  # 3
    ON_IDLE = "on-idle"  # 2


class EapIdentityEnum(Enum):
    """
    Enum for specifying the EAP peer identity type.
    """

    SEND_REQUEST = "send-request"  # 1
    USE_ID_PAYLOAD = "use-id-payload"  # 0


class Phase1EncapsulationEnum(Enum):
    """
    Enum to specify encapsulation methods for phase 1.
    """

    GRE = "gre"  # 1
    NONE = "none"  # 0
    VPN_ID_IPIP = "vpn-id-ipip"  # 3
    VXLAN = "vxlan"  # 2


class EncapsulationAddressEnum(Enum):
    """
    Enum to specify the source address for encapsulation.
    """

    IKE = "ike"  # 0
    IPV4 = "ipv4"  # 1
    IPV6 = "ipv6"  # 2


class EnforceUniqueIdEnum(Enum):
    """
    Enum to enforce unique ID check for peers.
    """

    DISABLE = "disable"  # 0
    KEEP_NEW = "keep-new"  # 1
    KEEP_OLD = "keep-old"  # 2


class PermissionsEnum(Enum):
    """
    Enum to specify different permission levels.
    """

    ALLOW = "allow"
    DISABLE = "disable"
    REQUIRE = "require"


class FecCodecEnum(Enum):
    """
    Enum to specify the Forward Error Correction codec.
    """

    RS = "rs"  # 1
    XOR = "xor"  # 2


class IkeVersionEnum(Enum):
    """
    Enum to specify the IKE protocol version.
    """

    V1 = "1"  # 1
    V2 = "2"  # 2


class IpFragmentationEnum(Enum):
    """
    Enum to determine IP packet fragmentation behavior.
    """

    POST_ENCAPSULATION = "post-encapsulation"  # 1
    PRE_ENCAPSULATION = "pre-encapsulation"  # 0


class IpVersionEnum(Enum):
    """
    Enum to specify the IP version.
    """

    V4 = "4"  # 1
    V6 = "6"  # 2


class IpsecTunnelSlotEnum(Enum):
    """
    Enum to specify the slot for IPsec tunnel establishment.
    """

    FPC1 = "FPC1"  # 3
    FPC10 = "FPC10"  # 12
    FPC2 = "FPC2"  # 4
    FPC3 = "FPC3"  # 5
    FPC4 = "FPC4"  # 6
    FPC5 = "FPC5"  # 7
    FPC6 = "FPC6"  # 8
    FPC7 = "FPC7"  # 9
    FPC8 = "FPC8"  # 10
    FPC9 = "FPC9"  # 11
    FPM10 = "FPM10"  # 20
    FPM11 = "FPM11"  # 21
    FPM12 = "FPM12"  # 22
    FPM3 = "FPM3"  # 13
    FPM4 = "FPM4"  # 14
    FPM5 = "FPM5"  # 15
    FPM6 = "FPM6"  # 16
    FPM7 = "FPM7"  # 17
    FPM8 = "FPM8"  # 18
    FPM9 = "FPM9"  # 19
    AUTO = "auto"  # 2
    MASTER = "master"  # 1


class LocalidTypeEnum(Enum):
    """
    Enum to specify the type of local ID.
    """

    ADDRESS = "address"  # 4
    ASN1DN = "asn1dn"  # 5
    AUTO = "auto"  # 0
    FQDN = "fqdn"  # 1
    KEYID = "keyid"  # 3
    USER_FQDN = "user-fqdn"  # 2


class MeshSelectorTypeEnum(Enum):
    """
    Enum to specify the type of mesh selector.
    """

    DISABLE = "disable"  # 0
    HOST = "host"  # 2
    SUBNET = "subnet"  # 1


class ModeEnum(Enum):
    """
    Enum to specify the ID protection mode.
    """

    AGGRESSIVE = "aggressive"  # 2
    MAIN = "main"  # 1


class MonitorHoldDownTypeEnum(Enum):
    """
    Enum to specify the hold-down type for monitoring.
    """

    DELAY = "delay"  # 1
    IMMEDIATE = "immediate"  # 0
    TIME = "time"  # 2


class MonitorHoldDownWeekdayEnum(Enum):
    """
    Enum to specify the day of the week for recovery after primary re-establishes.
    """

    EVERYDAY = "everyday"  # 128
    FRIDAY = "friday"  # 32
    MONDAY = "monday"  # 2
    SATURDAY = "saturday"  # 64
    SUNDAY = "sunday"  # 1
    THURSDAY = "thursday"  # 16
    TUESDAY = "tuesday"  # 4
    WEDNESDAY = "wednesday"  # 8


class NattraversalEnum(Enum):
    """
    Enum to specify NAT traversal behavior.
    """

    DISABLE = "disable"  # 0
    ENABLE = "enable"  # 1
    FORCED = "forced"  # 22


class PeertypeEnum(Enum):
    """
    Enum to specify the type of peer.
    """

    ANY = "any"  # 1
    DIALUP = "dialup"  # 4
    ONE = "one"  # 2
    PEER = "peer"  # 8
    PEERGRP = "peergrp"  # 16


class Phase1ProposalEnum(Enum):
    """
    Enum to specify the phase 1 proposal for IPsec.
    """

    DES3_MD5 = "3des-md5"  # 7
    DES3_SHA1 = "3des-sha1"  # 8
    DES3_SHA256 = "3des-sha256"  # 20
    DES3_SHA384 = "3des-sha384"  # 26
    DES3_SHA512 = "3des-sha512"  # 27
    AES128_MD5 = "aes128-md5"  # 9
    AES128_SHA1 = "aes128-sha1"  # 10
    AES128_SHA256 = "aes128-sha256"  # 21
    AES128_SHA384 = "aes128-sha384"  # 28
    AES128_SHA512 = "aes128-sha512"  # 29
    AES128GCM_PRFSHA1 = "aes128gcm-prfsha1"  # 65
    AES128GCM_PRFSHA256 = "aes128gcm-prfsha256"  # 66
    AES128GCM_PRFSHA384 = "aes128gcm-prfsha384"  # 67
    AES128GCM_PRFSHA512 = "aes128gcm-prfsha512"  # 68
    AES192_MD5 = "aes192-md5"  # 11
    AES192_SHA1 = "aes192-sha1"  # 12
    AES192_SHA256 = "aes192-sha256"  # 22
    AES192_SHA384 = "aes192-sha384"  # 30
    AES192_SHA512 = "aes192-sha512"  # 31
    AES256_MD5 = "aes256-md5"  # 13
    AES256_SHA1 = "aes256-sha1"  # 14
    AES256_SHA256 = "aes256-sha256"  # 23
    AES256_SHA384 = "aes256-sha384"  # 32
    AES256_SHA512 = "aes256-sha512"  # 33
    AES256GCM_PRFSHA1 = "aes256gcm-prfsha1"  # 69
    AES256GCM_PRFSHA256 = "aes256gcm-prfsha256"  # 70
    AES256GCM_PRFSHA384 = "aes256gcm-prfsha384"  # 71
    AES256GCM_PRFSHA512 = "aes256gcm-prfsha512"  # 72
    ARIA128_MD5 = "aria128-md5"  # 39
    ARIA128_SHA1 = "aria128-sha1"  # 40
    ARIA128_SHA256 = "aria128-sha256"  # 41
    ARIA128_SHA384 = "aria128-sha384"  # 42
    ARIA128_SHA512 = "aria128-sha512"  # 43
    ARIA192_MD5 = "aria192-md5"  # 45
    ARIA192_SHA1 = "aria192-sha1"  # 46
    ARIA192_SHA256 = "aria192-sha256"  # 47
    ARIA192_SHA384 = "aria192-sha384"  # 48
    ARIA192_SHA512 = "aria192-sha512"  # 49
    ARIA256_MD5 = "aria256-md5"  # 51
    ARIA256_SHA1 = "aria256-sha1"  # 52
    ARIA256_SHA256 = "aria256-sha256"  # 53
    ARIA256_SHA384 = "aria256-sha384"  # 54
    ARIA256_SHA512 = "aria256-sha512"  # 55
    CHACHA20POLY1305_PRFSHA1 = "chacha20poly1305-prfsha1"  # 73
    CHACHA20POLY1305_PRFSHA256 = "chacha20poly1305-prfsha256"  # 74
    CHACHA20POLY1305_PRFSHA384 = "chacha20poly1305-prfsha384"  # 75
    CHACHA20POLY1305_PRFSHA512 = "chacha20poly1305-prfsha512"  # 76
    DES_MD5 = "des-md5"  # 5
    DES_SHA1 = "des-sha1"  # 6
    DES_SHA256 = "des-sha256"  # 19
    DES_SHA384 = "des-sha384"  # 24
    DES_SHA512 = "des-sha512"  # 25
    SEED_MD5 = "seed-md5"  # 57
    SEED_SHA1 = "seed-sha1"  # 58
    SEED_SHA256 = "seed-sha256"  # 59
    SEED_SHA384 = "seed-sha384"  # 60
    SEED_SHA512 = "seed-sha512"  # 61


class RemoteGwMatchEnum(Enum):
    """
    Enum to specify the type of remote gateway address matching.
    """

    ANY = "any"  # 1
    GEOGRAPHY = "geography"  # 4
    IPMASK = "ipmask"  # 2
    IPRANGE = "iprange"  # 3


class RemoteGw6MatchEnum(Enum):
    """
    Enum to specify the type of IPv6 remote gateway address matching.
    """

    ANY = "any"  # 1
    GEOGRAPHY = "geography"  # 4
    IPPREFIX = "ipprefix"  # 5
    IPRANGE = "iprange"  # 3


class RsaSignatureFormatEnum(Enum):
    """
    Enum to specify the RSA signature format.
    """

    PKCS1 = "pkcs1"  # 0
    PSS = "pss"  # 1


class SignatureHashAlgEnum(Enum):
    """
    Enum to specify the digital signature hash algorithm.
    """

    SHA1 = "sha1"  # 2048
    SHA2_256 = "sha2-256"  # 4096
    SHA2_384 = "sha2-384"  # 8192
    SHA2_512 = "sha2-512"  # 32768


class SuiteBEnum(Enum):
    """
    Enum to specify the use of Suite-B.
    """

    DISABLE = "disable"  # 0
    SUITE_B_GCM_128 = "suite-b-gcm-128"  # 1
    SUITE_B_GCM_256 = "suite-b-gcm-256"  # 2


class TypeEnum(Enum):
    """
    Enum to specify the type of remote gateway.
    """

    DDNS = "ddns"  # 2
    DYNAMIC = "dynamic"  # 1
    STATIC = "static"  # 0


class WizardTypeEnum(Enum):
    """
    Enum to specify the type of VPN Wizard in the GUI.
    """

    CUSTOM = "custom"  # 0
    DIALUP_ANDROID = "dialup-android"  # 3
    DIALUP_CISCO = "dialup-cisco"  # 4
    DIALUP_CISCO_FW = "dialup-cisco-fw"  # 9
    DIALUP_FORTICLIENT = "dialup-forticlient"  # 1
    DIALUP_FORTIGATE = "dialup-fortigate"  # 8
    DIALUP_IOS = "dialup-ios"  # 2
    DIALUP_WINDOWS = "dialup-windows"  # 7
    HUB_FORTIGATE_AUTO_DISCOVERY = "hub-fortigate-auto-discovery"  # 11
    SIMPLIFIED_STATIC_FORTIGATE = "simplified-static-fortigate"  # 10
    SPOKE_FORTIGATE_AUTO_DISCOVERY = "spoke-fortigate-auto-discovery"  # 12
    STATIC_CISCO = "static-cisco"  # 6
    STATIC_FORTIGATE = "static-fortigate"  # 5


class XauthtypeEnum(Enum):
    """
    Enum to specify the type of XAuth.
    """

    AUTO = "auto"  # 16
    CHAP = "chap"  # 8
    CLIENT = "client"  # 2
    DISABLE = "disable"  # 1
    PAP = "pap"  # 4


class NetworkFeatureEnum(Enum):
    """
    Enum to specify network features.
    """

    DISABLE = "disable"
    ENABLE = "enable"
    PHASE1 = "phase1"


class DhgrpEnum(Enum):
    """
    Enum to specify the DH group.
    """

    DHGRP_1 = "1"  # 1
    DHGRP_14 = "14"  # 8
    DHGRP_15 = "15"  # 16
    DHGRP_16 = "16"  # 32
    DHGRP_17 = "17"  # 64
    DHGRP_18 = "18"  # 128
    DHGRP_19 = "19"  # 256
    DHGRP_2 = "2"  # 2
    DHGRP_20 = "20"  # 512
    DHGRP_21 = "21"  # 1024
    DHGRP_27 = "27"  # 2048
    DHGRP_28 = "28"  # 4096
    DHGRP_29 = "29"  # 8192
    DHGRP_30 = "30"  # 16384
    DHGRP_31 = "31"  # 32768
    DHGRP_32 = "32"  # 65536
    DHGRP_5 = "5"  # 4


class AddrTypeEnum(Enum):
    """
    Enum to specify the type of address.
    """

    IP = "ip"  # 2
    IP6 = "ip6"  # 6
    NAME = "name"  # 3
    NAME6 = "name6"  # 7
    RANGE = "range"  # 1
    RANGE6 = "range6"  # 5
    SUBNET = "subnet"  # 0
    SUBNET6 = "subnet6"  # 4


class Phase2EncapsulationEnum(Enum):
    """
    Enum to specify encapsulation methods for phase 2.
    """

    TRANSPORT_MODE = "transport-mode"  # 1
    TUNNEL_MODE = "tunnel-mode"  # 0


class KeylifeTypeEnum(Enum):
    """
    Enum to specify the type of key life.
    """

    BOTH = "both"  # 3
    KBS = "kbs"  # 2
    SECONDS = "seconds"  # 1


class Phase2ProposalEnum(Enum):
    """
    Enum to specify the phase 2 proposal for IPsec.
    """

    DES3_MD5 = "3des-md5"  # 7
    DES3_NULL = "3des-null"  # 4
    DES3_SHA1 = "3des-sha1"  # 8
    DES3_SHA256 = "3des-sha256"  # 20
    DES3_SHA384 = "3des-sha384"  # 26
    DES3_SHA512 = "3des-sha512"  # 27
    AES128_MD5 = "aes128-md5"  # 9
    AES128_NULL = "aes128-null"  # 15
    AES128_SHA1 = "aes128-sha1"  # 10
    AES128_SHA256 = "aes128-sha256"  # 21
    AES128_SHA384 = "aes128-sha384"  # 28
    AES128_SHA512 = "aes128-sha512"  # 29
    AES128GCM = "aes128gcm"  # 62
    AES192_MD5 = "aes192-md5"  # 11
    AES192_NULL = "aes192-null"  # 16
    AES192_SHA1 = "aes192-sha1"  # 12
    AES192_SHA256 = "aes192-sha256"  # 22
    AES192_SHA384 = "aes192-sha384"  # 30
    AES192_SHA512 = "aes192-sha512"  # 31
    AES256_MD5 = "aes256-md5"  # 13
    AES256_NULL = "aes256-null"  # 17
    AES256_SHA1 = "aes256-sha1"  # 14
    AES256_SHA256 = "aes256-sha256"  # 23
    AES256_SHA384 = "aes256-sha384"  # 32
    AES256_SHA512 = "aes256-sha512"  # 33
    AES256GCM = "aes256gcm"  # 63
    ARIA128_MD5 = "aria128-md5"  # 39
    ARIA128_NULL = "aria128-null"  # 38
    ARIA128_SHA1 = "aria128-sha1"  # 40
    ARIA128_SHA256 = "aria128-sha256"  # 41
    ARIA128_SHA384 = "aria128-sha384"  # 42
    ARIA128_SHA512 = "aria128-sha512"  # 43
    ARIA192_MD5 = "aria192-md5"  # 45
    ARIA192_NULL = "aria192-null"  # 44
    ARIA192_SHA1 = "aria192-sha1"  # 46
    ARIA192_SHA256 = "aria192-sha256"  # 47
    ARIA192_SHA384 = "aria192-sha384"  # 48
    ARIA192_SHA512 = "aria192-sha512"  # 49
    ARIA256_MD5 = "aria256-md5"  # 51
    ARIA256_NULL = "aria256-null"  # 50
    ARIA256_SHA1 = "aria256-sha1"  # 52
    ARIA256_SHA256 = "aria256-sha256"  # 53
    ARIA256_SHA384 = "aria256-sha384"  # 54
    ARIA256_SHA512 = "aria256-sha512"  # 55
    CHACHA20POLY1305 = "chacha20poly1305"  # 64
    DES_MD5 = "des-md5"  # 5
    DES_NULL = "des-null"  # 3
    DES_SHA1 = "des-sha1"  # 6
    DES_SHA256 = "des-sha256"  # 19
    DES_SHA384 = "des-sha384"  # 24
    DES_SHA512 = "des-sha512"  # 25
    NULL_MD5 = "null-md5"  # 1
    NULL_SHA1 = "null-sha1"  # 2
    NULL_SHA256 = "null-sha256"  # 18
    NULL_SHA384 = "null-sha384"  # 34
    NULL_SHA512 = "null-sha512"  # 35
    SEED_MD5 = "seed-md5"  # 57
    SEED_NULL = "seed-null"  # 56
    SEED_SHA1 = "seed-sha1"  # 58
    SEED_SHA256 = "seed-sha256"  # 59
    SEED_SHA384 = "seed-sha384"  # 60
    SEED_SHA512 = "seed-sha512"  # 61


class RouteOverlapEnum(Enum):
    """
    Enum to specify the action for overlapping routes.
    """

    ALLOW = "allow"  # 3
    USE_NEW = "use-new"  # 2
    USE_OLD = "use-old"  # 1


class Ipv4ExcludeRange(BaseModel):
    """
    Configuration Method IPv4 exclude ranges.
    """

    end_ip: IPv4Address = Field(
        alias="end-ip",
        description="End of IPv4 exclusive range.",
    )
    id: int = Field(default=0, description="ID.", le=4294967295, ge=0)
    start_ip: IPv4Address = Field(
        alias="start-ip",
        description="Start of IPv4 exclusive range.",
    )


class Ipv6ExcludeRange(BaseModel):
    """
    Configuration method IPv6 exclude ranges.
    """

    end_ip: IPv6Address = Field(
        alias="end-ip", description="End of IPv6 exclusive range."
    )
    id: int = Field(default=0, description="ID.", le=4294967295, ge=0)
    start_ip: IPv6Address = Field(
        alias="start-ip", description="Start of IPv6 exclusive range."
    )


class VpnIpsecPhase1Interface(BaseModel):
    """
    Configure VPN remote gateway.
    """

    acct_verify: StatusEnum = Field(
        alias="acct-verify",
        default=StatusEnum.DISABLE,
        description="Enable/disable verification of RADIUS accounting record.",
    )
    add_gw_route: StatusEnum = Field(
        alias="add-gw-route",
        default=StatusEnum.DISABLE,
        description="Enable/disable automatically add a route to the remote gateway.",
    )
    add_route: StatusEnum = Field(
        alias="add-route",
        default=StatusEnum.ENABLE,
        description="Enable/disable control addition of a route to peer destination selector.",
    )
    aggregate_member: StatusEnum = Field(
        alias="aggregate-member",
        default=StatusEnum.DISABLE,
        description="Enable/disable use as an aggregate member.",
    )
    aggregate_weight: int = Field(
        alias="aggregate-weight",
        default=1,
        description="Link weight for aggregate.",
        le=100,
        ge=1,
    )
    assign_ip: StatusEnum = Field(
        alias="assign-ip",
        default=StatusEnum.ENABLE,
        description="Enable/disable assignment of IP to IPsec interface via configuration method.",
    )
    assign_ip_from: AssignIpFromEnum = Field(
        alias="assign-ip-from",
        default=AssignIpFromEnum.RANGE,
        description="Method by which the IP address will be assigned.",
    )
    authmethod: AuthmethodEnum = Field(
        default=AuthmethodEnum.PSK, description="Authentication method."
    )
    authmethod_remote: AuthmethodEnum = Field(
        ...,
        alias="authmethod-remote",
        description="Authentication method (remote side).",
    )
    authpasswd: str = Field(
        description="XAuth password (max 35 characters).",
    )
    authusr: str = Field(..., description="XAuth user name.", max_length=64)
    authusrgrp: list[str] = Field(..., description="Authentication user group.")
    auto_discovery_crossover: AutoDiscoveryCrossoverEnum = Field(
        alias="auto-discovery-crossover",
        default=AutoDiscoveryCrossoverEnum.ALLOW,
        description="Allow/block set-up of short-cut tunnels between different network IDs.",
    )
    auto_discovery_forwarder: StatusEnum = Field(
        alias="auto-discovery-forwarder",
        default=StatusEnum.DISABLE,
        description="Enable/disable forwarding auto-discovery short-cut messages.",
    )
    auto_discovery_offer_interval: int = Field(
        alias="auto-discovery-offer-interval",
        default=5,
        description="Interval between shortcut offer messages in seconds (1 - 300, default = 5).",
        le=300,
        ge=1,
    )
    auto_discovery_psk: StatusEnum = Field(
        alias="auto-discovery-psk",
        default=StatusEnum.DISABLE,
        description="Enable/disable use of pre-shared secrets for authentication of auto-discovery tunnels.",
    )
    auto_discovery_receiver: StatusEnum = Field(
        alias="auto-discovery-receiver",
        default=StatusEnum.DISABLE,
        description="Enable/disable accepting auto-discovery short-cut messages.",
    )
    auto_discovery_sender: StatusEnum = Field(
        alias="auto-discovery-sender",
        default=StatusEnum.DISABLE,
        description="Enable/disable sending auto-discovery short-cut messages.",
    )
    auto_discovery_shortcuts: AutoDiscoveryShortcutsEnum = Field(
        alias="auto-discovery-shortcuts",
        default=AutoDiscoveryShortcutsEnum.INDEPENDENT,
        description="Control deletion of child short-cut tunnels when the parent tunnel goes down.",
    )
    auto_negotiate: StatusEnum = Field(
        alias="auto-negotiate",
        default=StatusEnum.ENABLE,
        description="Enable/disable automatic initiation of IKE SA negotiation.",
    )
    azure_ad_autoconnect: StatusEnum = Field(
        alias="azure-ad-autoconnect",
        default=StatusEnum.DISABLE,
        description="Enable/disable Azure AD Auto-Connect for FortiClient.",
    )
    backup_gateway: list[str] = Field(
        default=[],
        alias="backup-gateway",
        description="Instruct unity clients about the backup gateway address(es).",
    )
    banner: str = Field(
        ...,
        description="Message that unity client should display after connecting.",
        max_length=1024,
    )
    cert_id_validation: StatusEnum = Field(
        alias="cert-id-validation",
        default=StatusEnum.ENABLE,
        description="Enable/disable cross validation of peer ID and the identity in the peer's certificate as specified in RFC 4945.",
    )
    cert_trust_store: CertTrustStoreEnum = Field(
        alias="cert-trust-store",
        default=CertTrustStoreEnum.LOCAL,
        description="CA certificate trust store.",
    )
    certificate: list[str] = Field(
        ..., description="The names of up to 4 signed personal certificates."
    )
    childless_ike: StatusEnum = Field(
        alias="childless-ike",
        default=StatusEnum.DISABLE,
        description="Enable/disable childless IKEv2 initiation (RFC 6023).",
    )
    client_auto_negotiate: StatusEnum = Field(
        alias="client-auto-negotiate",
        default=StatusEnum.DISABLE,
        description="Enable/disable allowing the VPN client to bring up the tunnel when there is no traffic.",
    )
    client_keep_alive: StatusEnum = Field(
        alias="client-keep-alive",
        default=StatusEnum.DISABLE,
        description="Enable/disable allowing the VPN client to keep the tunnel up when there is no traffic.",
    )
    comments: str = Field(..., description="Comment.", max_length=255)
    default_gw: IPv4Address = Field(
        alias="default-gw",
        description="IPv4 address of default route gateway to use for traffic exiting the interface.",
    )
    default_gw_priority: int = Field(
        alias="default-gw-priority",
        default=0,
        description="Priority for default gateway route. A higher priority number signifies a less preferred route.",
        le=4294967295,
        ge=0,
    )
    dev_id: str = Field(
        alias="dev-id",
        default="''",
        description="Device ID carried by the device ID notification.",
        max_length=63,
    )
    dev_id_notification: StatusEnum = Field(
        alias="dev-id-notification",
        default=StatusEnum.DISABLE,
        description="Enable/disable device ID notification.",
    )
    dhcp_ra_giaddr: IPv4Address = Field(
        alias="dhcp-ra-giaddr",
        description="Relay agent gateway IP address to use in the giaddr field of DHCP requests.",
    )
    dhcp6_ra_linkaddr: IPv6Address = Field(
        alias="dhcp6-ra-linkaddr",
        description="Relay agent IPv6 link address to use in DHCP6 requests.",
    )
    dhgrp: DhgrpEnum = Field(
        default="14 5",
        description="DH group. Can take on the values contained in the 'DhgrpEnum' enum separated by a space",
    )
    digital_signature_auth: StatusEnum = Field(
        alias="digital-signature-auth",
        default=StatusEnum.DISABLE,
        description="Enable/disable IKEv2 Digital Signature Authentication (RFC 7427).",
    )
    distance: int = Field(
        default=15,
        description="Distance for routes added by IKE (1 - 255).",
        le=255,
        ge=1,
    )
    dns_mode: DnsModeEnum = Field(
        alias="dns-mode", default=DnsModeEnum.MANUAL, description="DNS server mode."
    )
    domain: str = Field(
        ...,
        description="Instruct unity clients about the single default DNS domain.",
        max_length=63,
    )
    dpd: DpdEnum = Field(
        default=DpdEnum.ON_DEMAND, description="Dead Peer Detection mode."
    )
    dpd_retrycount: int = Field(
        alias="dpd-retrycount",
        default=3,
        description="Number of DPD retry attempts.",
        le=10,
        ge=0,
    )
    dpd_retryinterval: list[int] = Field(
        alias="dpd-retryinterval", default=[20], description="DPD retry interval."
    )
    eap: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable/disable IKEv2 EAP authentication.",
    )
    eap_exclude_peergrp: list[str] = Field(
        ...,
        alias="eap-exclude-peergrp",
        description="Peer group excluded from EAP authentication.",
    )
    eap_identity: EapIdentityEnum = Field(
        alias="eap-identity",
        default=EapIdentityEnum.USE_ID_PAYLOAD,
        description="IKEv2 EAP peer identity type.",
    )
    ems_sn_check: StatusEnum = Field(
        alias="ems-sn-check",
        default=StatusEnum.DISABLE,
        description="Enable/disable verification of EMS serial number.",
    )
    encap_local_gw4: IPv4Address = Field(
        alias="encap-local-gw4",
        description="Local IPv4 address of GRE/VXLAN tunnel.",
    )
    encap_local_gw6: IPv6Address = Field(
        alias="encap-local-gw6",
        description="Local IPv6 address of GRE/VXLAN tunnel.",
    )
    encap_remote_gw4: IPv4Address = Field(
        alias="encap-remote-gw4",
        description="Remote IPv4 address of GRE/VXLAN tunnel.",
    )
    encap_remote_gw6: IPv6Address = Field(
        alias="encap-remote-gw6",
        description="Remote IPv6 address of GRE/VXLAN tunnel.",
    )
    encapsulation: Phase1EncapsulationEnum = Field(
        default=Phase1EncapsulationEnum.NONE,
        description="Enable/disable GRE/VXLAN/VPNID encapsulation.",
    )
    encapsulation_address: EncapsulationAddressEnum = Field(
        alias="encapsulation-address",
        default=EncapsulationAddressEnum.IKE,
        description="Source for GRE/VXLAN tunnel address.",
    )
    enforce_unique_id: EnforceUniqueIdEnum = Field(
        alias="enforce-unique-id",
        default=EnforceUniqueIdEnum.DISABLE,
        description="Enable/disable peer ID uniqueness check.",
    )
    esn: PermissionsEnum = Field(
        default=PermissionsEnum.DISABLE,
        description="Extended sequence number (ESN) negotiation.",
    )
    exchange_fgt_device_id: StatusEnum = Field(
        alias="exchange-fgt-device-id",
        default=StatusEnum.DISABLE,
        description="Enable/disable device identifier exchange with peer FortiGate units for use of VPN monitor data by FortiManager.",
    )
    exchange_interface_ip: StatusEnum = Field(
        alias="exchange-interface-ip",
        default=StatusEnum.DISABLE,
        description="Enable/disable exchange of IPsec interface IP address.",
    )
    exchange_ip_addr4: IPv4Address = Field(
        alias="exchange-ip-addr4",
        description="IPv4 address to exchange with peers.",
    )
    exchange_ip_addr6: IPv6Address = Field(
        alias="exchange-ip-addr6",
        description="IPv6 address to exchange with peers.",
    )
    fec_base: int = Field(
        alias="fec-base",
        default=10,
        description="Number of base Forward Error Correction packets (1 - 20).",
        le=20,
        ge=1,
    )
    fec_codec: FecCodecEnum = Field(
        alias="fec-codec",
        default=FecCodecEnum.RS,
        description="Forward Error Correction encoding/decoding algorithm.",
    )
    fec_egress: StatusEnum = Field(
        alias="fec-egress",
        default=StatusEnum.DISABLE,
        description="Enable/disable Forward Error Correction for egress IPsec traffic.",
    )
    fec_health_check: list[str] = Field(
        ..., alias="fec-health-check", description="SD-WAN health check."
    )
    fec_ingress: StatusEnum = Field(
        alias="fec-ingress",
        default=StatusEnum.DISABLE,
        description="Enable/disable Forward Error Correction for ingress IPsec traffic.",
    )
    fec_mapping_profile: list[str] = Field(
        ...,
        alias="fec-mapping-profile",
        description="Forward Error Correction (FEC) mapping profile.",
    )
    fec_receive_timeout: int = Field(
        alias="fec-receive-timeout",
        default=50,
        description="Timeout in milliseconds before dropping Forward Error Correction packets (1 - 1000).",
        le=1000,
        ge=1,
    )
    fec_redundant: int = Field(
        alias="fec-redundant",
        default=1,
        description="Number of redundant Forward Error Correction packets (1 - 5 for reed-solomon, 1 for xor).",
        le=5,
        ge=1,
    )
    fec_send_timeout: int = Field(
        alias="fec-send-timeout",
        default=5,
        description="Timeout in milliseconds before sending Forward Error Correction packets (1 - 1000).",
        le=1000,
        ge=1,
    )
    fgsp_sync: StatusEnum = Field(
        alias="fgsp-sync",
        default=StatusEnum.DISABLE,
        description="Enable/disable IPsec syncing of tunnels for FGSP IPsec.",
    )
    forticlient_enforcement: StatusEnum = Field(
        alias="forticlient-enforcement",
        default=StatusEnum.DISABLE,
        description="Enable/disable FortiClient enforcement.",
    )
    fragmentation: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        description="Enable/disable fragment IKE message on re-transmission.",
    )
    fragmentation_mtu: int = Field(
        alias="fragmentation-mtu",
        default=1200,
        description="IKE fragmentation MTU (500 - 16000).",
        le=16000,
        ge=500,
    )
    group_authentication: StatusEnum = Field(
        alias="group-authentication",
        default=StatusEnum.DISABLE,
        description="Enable/disable IKEv2 IDi group authentication.",
    )
    group_authentication_secret: str = Field(
        alias="group-authentication-secret",
        description="Password for IKEv2 ID group authentication. ASCII string or hexadecimal indicated by a leading 0x.",
    )
    ha_sync_esp_seqno: StatusEnum = Field(
        alias="ha-sync-esp-seqno",
        default=StatusEnum.ENABLE,
        description="Enable/disable sequence number jump ahead for IPsec HA.",
    )
    idle_timeout: StatusEnum = Field(
        alias="idle-timeout",
        default=StatusEnum.DISABLE,
        description="Enable/disable IPsec tunnel idle timeout.",
    )
    idle_timeoutinterval: int = Field(
        alias="idle-timeoutinterval",
        default=15,
        description="IPsec tunnel idle timeout in minutes (5 - 43200).",
        le=43200,
        ge=5,
    )
    ike_version: IkeVersionEnum = Field(
        alias="ike-version",
        default=IkeVersionEnum.V1,
        description="IKE protocol version.",
    )
    inbound_dscp_copy: StatusEnum = Field(
        alias="inbound-dscp-copy",
        default=StatusEnum.DISABLE,
        description="Enable/disable copy the dscp in the ESP header to the inner IP Header.",
    )
    include_local_lan: StatusEnum = Field(
        alias="include-local-lan",
        default=StatusEnum.DISABLE,
        description="Enable/disable allow local LAN access on unity clients.",
    )
    interface: list[str] = Field(
        ..., description="Local physical, aggregate, or VLAN outgoing interface."
    )
    internal_domain_list: list[str] = Field(
        ...,
        alias="internal-domain-list",
        description="List of domains for which the client directs DNS queries to the internal DNS servers for resolution.  DNS servers are configured in the mode-cfg settings.  One or more internal domain names in quotes separated by spaces, like 'abc.com xyz.com 123.com'",
    )
    ip_delay_interval: int = Field(
        alias="ip-delay-interval",
        default=0,
        description="IP address reuse delay interval in seconds (0 - 28800).",
        le=28800,
        ge=0,
    )
    ip_fragmentation: IpFragmentationEnum = Field(
        alias="ip-fragmentation",
        default=IpFragmentationEnum.POST_ENCAPSULATION,
        description="Determine whether IP packets are fragmented before or after IPsec encapsulation.",
    )
    ip_version: IpVersionEnum = Field(
        alias="ip-version",
        default=IpVersionEnum.V4,
        description="IP version to use for VPN interface.",
    )
    ipsec_tunnel_slot: IpsecTunnelSlotEnum = Field(
        alias="ipsec-tunnel-slot",
        default=IpsecTunnelSlotEnum.AUTO,
        description="Slot at which IPsec tunnel will be establishd.",
    )
    ipv4_dns_server1: IPv4Address = Field(
        alias="ipv4-dns-server1",
        description="IPv4 DNS server 1.",
    )
    ipv4_dns_server2: IPv4Address = Field(
        alias="ipv4-dns-server2",
        description="IPv4 DNS server 2.",
    )
    ipv4_dns_server3: IPv4Address = Field(
        alias="ipv4-dns-server3",
        description="IPv4 DNS server 3.",
    )
    ipv4_end_ip: IPv4Address = Field(
        alias="ipv4-end-ip",
        description="End of IPv4 range.",
    )
    ipv4_name: list[str] = Field(
        ..., alias="ipv4-name", description="IPv4 address name."
    )
    ipv4_netmask: str = Field(
        alias="ipv4-netmask", default="255.255.255.255", description="IPv4 Netmask."
    )
    ipv4_split_exclude: list[str] = Field(
        ...,
        alias="ipv4-split-exclude",
        description="IPv4 subnets that should not be sent over the IPsec tunnel.",
    )
    ipv4_split_include: list[str] = Field(
        ..., alias="ipv4-split-include", description="IPv4 split-include subnets."
    )
    ipv4_start_ip: IPv4Address = Field(
        alias="ipv4-start-ip",
        description="Start of IPv4 range.",
    )
    ipv4_wins_server1: IPv4Address = Field(
        alias="ipv4-wins-server1",
        description="WINS server 1.",
    )
    ipv4_wins_server2: IPv4Address = Field(
        alias="ipv4-wins-server2",
        description="WINS server 2.",
    )
    ipv6_dns_server1: IPv6Address = Field(
        alias="ipv6-dns-server1", description="IPv6 DNS server 1."
    )
    ipv6_dns_server2: IPv6Address = Field(
        alias="ipv6-dns-server2", description="IPv6 DNS server 2."
    )
    ipv6_dns_server3: IPv6Address = Field(
        alias="ipv6-dns-server3", description="IPv6 DNS server 3."
    )
    ipv6_end_ip: IPv6Address = Field(
        alias="ipv6-end-ip", description="End of IPv6 range."
    )
    ipv6_name: list[str] = Field(
        ..., alias="ipv6-name", description="IPv6 address name."
    )
    ipv6_prefix: int = Field(
        alias="ipv6-prefix", default=128, description="IPv6 prefix.", le=128, ge=1
    )
    ipv6_split_exclude: list[str] = Field(
        ...,
        alias="ipv6-split-exclude",
        description="IPv6 subnets that should not be sent over the IPsec tunnel.",
    )
    ipv6_split_include: list[str] = Field(
        ..., alias="ipv6-split-include", description="IPv6 split-include subnets."
    )
    ipv6_start_ip: IPv6Address = Field(
        alias="ipv6-start-ip", description="Start of IPv6 range."
    )
    keepalive: int = Field(
        default=10, description="NAT-T keep alive interval.", le=900, ge=10
    )
    keylife: int = Field(
        default=86400,
        description="Time to wait in seconds before phase 1 encryption key expires.",
        le=172800,
        ge=120,
    )
    link_cost: int = Field(
        alias="link-cost",
        default=0,
        description="VPN tunnel underlay link cost.",
        le=255,
        ge=0,
    )
    local_gw: IPv4Address = Field(
        alias="local-gw",
        description="IPv4 address of the local gateway's external interface.",
    )
    local_gw6: IPv6Address = Field(
        alias="local-gw6",
        description="IPv6 address of the local gateway's external interface.",
    )
    localid: str = Field(..., description="Local ID.", max_length=63)
    localid_type: LocalidTypeEnum = Field(
        alias="localid-type", default=LocalidTypeEnum.AUTO, description="Local ID type."
    )
    loopback_asymroute: StatusEnum = Field(
        alias="loopback-asymroute",
        default=StatusEnum.ENABLE,
        description="Enable/disable asymmetric routing for IKE traffic on loopback interface.",
    )
    mesh_selector_type: MeshSelectorTypeEnum = Field(
        alias="mesh-selector-type",
        default=MeshSelectorTypeEnum.DISABLE,
        description="Add selectors containing subsets of the configuration depending on traffic.",
    )
    mode: ModeEnum = Field(
        default=ModeEnum.MAIN,
        description="The ID protection mode used to establish a secure channel.",
    )
    mode_cfg: StatusEnum = Field(
        alias="mode-cfg",
        default=StatusEnum.DISABLE,
        description="Enable/disable configuration method.",
    )
    mode_cfg_allow_client_selector: StatusEnum = Field(
        alias="mode-cfg-allow-client-selector",
        default=StatusEnum.DISABLE,
        description="Enable/disable mode-cfg client to use custom phase2 selectors.",
    )
    monitor: list[str] = Field(
        ..., description="IPsec interface as backup for primary interface."
    )
    monitor_hold_down_delay: int = Field(
        alias="monitor-hold-down-delay",
        default=0,
        description="Time to wait in seconds before recovery once primary re-establishes.",
        le=31536000,
        ge=0,
    )
    monitor_hold_down_time: str = Field(
        alias="monitor-hold-down-time",
        default="00:00",
        description="Time of day at which to fail back to primary after it re-establishes.",
    )
    monitor_hold_down_type: MonitorHoldDownTypeEnum = Field(
        alias="monitor-hold-down-type",
        default=MonitorHoldDownTypeEnum.IMMEDIATE,
        description="Recovery time method when primary interface re-establishes.",
    )
    monitor_hold_down_weekday: MonitorHoldDownWeekdayEnum = Field(
        alias="monitor-hold-down-weekday",
        default=MonitorHoldDownWeekdayEnum.SUNDAY,
        description="Day of the week to recover once primary re-establishes.",
    )
    name: str = Field(..., description="IPsec remote gateway name.", max_length=15)
    nattraversal: NattraversalEnum = Field(
        default=NattraversalEnum.ENABLE, description="Enable/disable NAT traversal."
    )
    negotiate_timeout: int = Field(
        alias="negotiate-timeout",
        default=30,
        description="IKE SA negotiation timeout in seconds (1 - 300).",
        le=300,
        ge=1,
    )
    net_device: StatusEnum = Field(
        alias="net-device",
        default=StatusEnum.DISABLE,
        description="Enable/disable kernel device creation.",
    )
    network_id: int = Field(
        alias="network-id",
        default=0,
        description="VPN gateway network ID.",
        le=255,
        ge=0,
    )
    network_overlay: StatusEnum = Field(
        alias="network-overlay",
        default=StatusEnum.DISABLE,
        description="Enable/disable network overlays.",
    )
    npu_offload: StatusEnum = Field(
        alias="npu-offload",
        default=StatusEnum.ENABLE,
        description="Enable/disable offloading NPU.",
    )
    packet_redistribution: StatusEnum = Field(
        alias="packet-redistribution",
        default=StatusEnum.DISABLE,
        description="Enable/disable packet distribution (RPS) on the IPsec interface.",
    )
    passive_mode: StatusEnum = Field(
        alias="passive-mode",
        default=StatusEnum.DISABLE,
        description="Enable/disable IPsec passive mode for static tunnels.",
    )
    peer: list[str] = Field(..., description="Accept this peer certificate.")
    peergrp: list[str] = Field(..., description="Accept this peer certificate group.")
    peerid: str = Field(..., description="Accept this peer identity.", max_length=255)
    peertype: PeertypeEnum = Field(
        default=PeertypeEnum.PEER, description="Accept this peer type."
    )
    ppk: PermissionsEnum = Field(
        default=PermissionsEnum.DISABLE,
        description="Enable/disable IKEv2 Postquantum Preshared Key (PPK).",
    )
    ppk_identity: str = Field(
        ...,
        alias="ppk-identity",
        description="IKEv2 Postquantum Preshared Key Identity.",
        max_length=35,
    )
    ppk_secret: str = Field(
        alias="ppk-secret",
        description="IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal encoded with a leading 0x).",
    )
    priority: int = Field(
        default=1,
        description="Priority for routes added by IKE (1 - 65535).",
        le=65535,
        ge=1,
    )
    proposal: Phase1ProposalEnum = Field(..., description="Phase1 proposal.")
    psksecret: str = Field(
        description="Pre-shared secret for PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).",
    )
    psksecret_remote: str = Field(
        alias="psksecret-remote",
        description="Pre-shared secret for remote side PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).",
    )
    reauth: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable/disable re-authentication upon IKE SA lifetime expiration.",
    )
    rekey: StatusEnum = Field(
        default=StatusEnum.ENABLE, description="Enable/disable phase1 rekey."
    )
    remote_gw: IPv4Address = Field(
        alias="remote-gw",
        description="IPv4 address of the remote gateway's external interface.",
    )
    remote_gw_country: str = Field(
        ...,
        alias="remote-gw-country",
        description="IPv4 addresses associated to a specific country.",
        max_length=2,
    )
    remote_gw_end_ip: IPv4Address = Field(
        alias="remote-gw-end-ip",
        description="Last IPv4 address in the range.",
    )
    remote_gw_match: RemoteGwMatchEnum = Field(
        alias="remote-gw-match",
        default=RemoteGwMatchEnum.ANY,
        description="Set type of IPv4 remote gateway address matching.",
    )
    remote_gw_start_ip: IPv4Address = Field(
        alias="remote-gw-start-ip",
        description="First IPv4 address in the range.",
    )
    remote_gw_subnet: IPv4Address = Field(
        alias="remote-gw-subnet",
        description="IPv4 address and subnet mask.",
    )
    remote_gw6: IPv6Address = Field(
        alias="remote-gw6",
        description="IPv6 address of the remote gateway's external interface.",
    )
    remote_gw6_country: str = Field(
        ...,
        alias="remote-gw6-country",
        description="IPv6 addresses associated to a specific country.",
        max_length=2,
    )
    remote_gw6_end_ip: IPv6Address = Field(
        alias="remote-gw6-end-ip",
        description="Last IPv6 address in the range.",
    )
    remote_gw6_match: RemoteGw6MatchEnum = Field(
        alias="remote-gw6-match",
        default=RemoteGw6MatchEnum.ANY,
        description="Set type of IPv6 remote gateway address matching.",
    )
    remote_gw6_start_ip: IPv6Address = Field(
        alias="remote-gw6-start-ip",
        description="First IPv6 address in the range.",
    )
    remote_gw6_subnet: IPv6Address = Field(
        alias="remote-gw6-subnet",
        description="IPv6 address and prefix.",
    )
    remotegw_ddns: str = Field(
        ...,
        alias="remotegw-ddns",
        description="Domain name of remote gateway. For example, name.ddns.com.",
        max_length=63,
    )
    rsa_signature_format: RsaSignatureFormatEnum = Field(
        alias="rsa-signature-format",
        default=RsaSignatureFormatEnum.PKCS1,
        description="Digital Signature Authentication RSA signature format.",
    )
    rsa_signature_hash_override: StatusEnum = Field(
        alias="rsa-signature-hash-override",
        default=StatusEnum.DISABLE,
        description="Enable/disable IKEv2 RSA signature hash algorithm override.",
    )
    save_password: StatusEnum = Field(
        alias="save-password",
        default=StatusEnum.DISABLE,
        description="Enable/disable saving XAuth username and password on VPN clients.",
    )
    send_cert_chain: StatusEnum = Field(
        alias="send-cert-chain",
        default=StatusEnum.ENABLE,
        description="Enable/disable sending certificate chain.",
    )
    signature_hash_alg: str = Field(
        alias="signature-hash-alg",
        default="sha2-512 sha2-384 sha2-256 sha1",
        description="Digital Signature Authentication hash algorithms. Can take on the values contained in the 'SignatureHashAlgEnum' enum separated by a space",
    )
    split_include_service: list[str] = Field(
        ..., alias="split-include-service", description="Split-include services."
    )
    suite_b: SuiteBEnum = Field(
        alias="suite-b", default=SuiteBEnum.DISABLE, description="Use Suite-B."
    )
    transit_gateway: StatusEnum = Field(
        alias="transit-gateway",
        default=StatusEnum.DISABLE,
        description="IPsec tunnel created by autoscaling to be used as a transit gateway.",
    )
    type: TypeEnum = Field(default=TypeEnum.STATIC, description="Remote gateway type.")
    unity_support: StatusEnum = Field(
        alias="unity-support",
        default=StatusEnum.ENABLE,
        description="Enable/disable support for Cisco UNITY Configuration Method extensions.",
    )
    usrgrp: list[str] = Field(..., description="User group name for dialup peers.")
    vni: int = Field(default=0, description="VNI of VXLAN tunnel.", le=16777215, ge=1)
    wizard_type: WizardTypeEnum = Field(
        alias="wizard-type",
        default=WizardTypeEnum.CUSTOM,
        description="GUI VPN Wizard Type.",
    )
    xauthtype: XauthtypeEnum = Field(
        default=XauthtypeEnum.DISABLE, description="XAuth type."
    )
    ipv4_exclude_range: list[Ipv4ExcludeRange] | None = Field(
        alias="ipv4-exclude-range",
        default=None,
        description="Configuration Method IPv4 exclude ranges.",
    )
    ipv6_exclude_range: list[Ipv6ExcludeRange] | None = Field(
        alias="ipv6-exclude-range",
        default=None,
        description="Configuration method IPv6 exclude ranges.",
    )


class VpnIpsecPhase2Interface(BaseModel):
    """
    Configure VPN autokey tunnel.
    """

    add_route: NetworkFeatureEnum = Field(
        alias="add-route",
        default=NetworkFeatureEnum.PHASE1,
        description="Enable/disable automatic route addition.",
    )
    auto_discovery_forwarder: NetworkFeatureEnum = Field(
        alias="auto-discovery-forwarder",
        default=NetworkFeatureEnum.PHASE1,
        description="Enable/disable forwarding short-cut messages.",
    )
    auto_discovery_sender: NetworkFeatureEnum = Field(
        alias="auto-discovery-sender",
        default=NetworkFeatureEnum.PHASE1,
        description="Enable/disable sending short-cut messages.",
    )
    auto_negotiate: StatusEnum = Field(
        alias="auto-negotiate",
        default=StatusEnum.DISABLE,
        description="Enable/disable IPsec SA auto-negotiation.",
    )
    comments: str = Field(..., description="Comment.", max_length=255)
    dhcp_ipsec: StatusEnum = Field(
        alias="dhcp-ipsec",
        default=StatusEnum.DISABLE,
        description="Enable/disable DHCP-IPsec.",
    )
    dhgrp: str = Field(
        default="14 5",
        description="Phase2 DH group. Can take on the values contained in the 'DhgrpEnum' enum separated by a space",
    )
    diffserv: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable/disable applying DSCP value to the IPsec tunnel outer IP header.",
    )
    diffservcode: str = Field(
        default="000000",
        description="DSCP value to be applied to the IPsec tunnel outer IP header.",
    )
    dst_addr_type: AddrTypeEnum = Field(
        alias="dst-addr-type",
        default=AddrTypeEnum.SUBNET,
        description="Remote proxy ID type.",
    )
    dst_end_ip: IPv4Address = Field(
        alias="dst-end-ip",
        description="Remote proxy ID IPv4 end.",
    )
    dst_end_ip6: IPv6Address = Field(
        alias="dst-end-ip6", description="Remote proxy ID IPv6 end."
    )
    dst_name: list[str] = Field(
        ..., alias="dst-name", description="Remote proxy ID name."
    )
    dst_name6: list[str] = Field(
        ..., alias="dst-name6", description="Remote proxy ID name."
    )
    dst_port: int = Field(
        alias="dst-port",
        default=0,
        description="Quick mode destination port (1 - 65535 or 0 for all).",
        le=65535,
        ge=0,
    )
    dst_start_ip: IPv4Address = Field(
        alias="dst-start-ip",
        description="Remote proxy ID IPv4 start.",
    )
    dst_start_ip6: IPv6Address = Field(
        alias="dst-start-ip6", description="Remote proxy ID IPv6 start."
    )
    dst_subnet: IPv4Address = Field(
        alias="dst-subnet",
        description="Remote proxy ID IPv4 subnet.",
    )
    dst_subnet6: IPv6Address = Field(
        alias="dst-subnet6", description="Remote proxy ID IPv6 subnet."
    )
    encapsulation: Phase2EncapsulationEnum = Field(
        default=Phase2EncapsulationEnum.TUNNEL_MODE,
        description="ESP encapsulation mode.",
    )
    inbound_dscp_copy: NetworkFeatureEnum = Field(
        alias="inbound-dscp-copy",
        default=NetworkFeatureEnum.PHASE1,
        description="Enable/disable copying of the DSCP in the ESP header to the inner IP header.",
    )
    initiator_ts_narrow: StatusEnum = Field(
        alias="initiator-ts-narrow",
        default=StatusEnum.DISABLE,
        description="Enable/disable traffic selector narrowing for IKEv2 initiator.",
    )
    ipv4_df: StatusEnum = Field(
        alias="ipv4-df",
        default=StatusEnum.DISABLE,
        description="Enable/disable setting and resetting of IPv4 'Don't Fragment' bit.",
    )
    keepalive: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable keep alive."
    )
    keylife_type: KeylifeTypeEnum = Field(
        alias="keylife-type",
        default=KeylifeTypeEnum.SECONDS,
        description="Keylife type.",
    )
    keylifekbs: int = Field(
        default=5120,
        description="Phase2 key life in number of kilobytes of traffic (5120 - 4294967295).",
        le=4294967295,
        ge=5120,
    )
    keylifeseconds: int = Field(
        default=43200,
        description="Phase2 key life in time in seconds (120 - 172800).",
        le=172800,
        ge=120,
    )
    l2tp: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable L2TP over IPsec."
    )
    name: str = Field(..., description="IPsec tunnel name.", max_length=35)
    pfs: StatusEnum = Field(
        default=StatusEnum.ENABLE, description="Enable/disable PFS feature."
    )
    phase1name: list[str] = Field(
        ..., description="Phase 1 determines the options required for phase 2."
    )
    proposal: Phase2ProposalEnum = Field(..., description="Phase2 proposal.")
    protocol: int = Field(
        default=0,
        description="Quick mode protocol selector (1 - 255 or 0 for all).",
        le=255,
        ge=0,
    )
    replay: StatusEnum = Field(
        default=StatusEnum.ENABLE, description="Enable/disable replay detection."
    )
    route_overlap: RouteOverlapEnum = Field(
        alias="route-overlap",
        default=RouteOverlapEnum.USE_NEW,
        description="Action for overlapping routes.",
    )
    single_source: StatusEnum = Field(
        alias="single-source",
        default=StatusEnum.DISABLE,
        description="Enable/disable single source IP restriction.",
    )
    src_addr_type: AddrTypeEnum = Field(
        alias="src-addr-type",
        default=AddrTypeEnum.SUBNET,
        description="Local proxy ID type.",
    )
    src_end_ip: IPv4Address = Field(
        alias="src-end-ip",
        description="Local proxy ID end.",
    )
    src_end_ip6: IPv6Address = Field(
        alias="src-end-ip6", description="Local proxy ID IPv6 end."
    )
    src_name: list[str] = Field(
        ..., alias="src-name", description="Local proxy ID name."
    )
    src_name6: list[str] = Field(
        ..., alias="src-name6", description="Local proxy ID name."
    )
    src_port: int = Field(
        alias="src-port",
        default=0,
        description="Quick mode source port (1 - 65535 or 0 for all).",
        le=65535,
        ge=0,
    )
    src_start_ip: IPv4Address = Field(
        alias="src-start-ip",
        description="Local proxy ID start.",
    )
    src_start_ip6: IPv6Address = Field(
        alias="src-start-ip6", description="Local proxy ID IPv6 start."
    )
    src_subnet: IPv4Address = Field(
        alias="src-subnet",
        description="Local proxy ID subnet.",
    )
    src_subnet6: IPv6Address = Field(
        alias="src-subnet6", description="Local proxy ID IPv6 subnet."
    )


class SystemInterface(BaseModel):
    """
    system interface model
    """

    ip: str = Field(
        default=DEFAULT_NETWORK,
        description="ip.",
    )
    remote_ip: str = Field(
        alias="remote-ip",
        default=DEFAULT_NETWORK,
        description="ip.",
    )


class FortiManagerUpdateIPSec(BaseModel):
    """
    fortimanager update ipsec model
    """

    name: str = Field(..., description="ipsec tunnel template name.")
    automatic_routing: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="automatic-routing",
        description="enable / disable automatic routing.",
    )
    local_addr_type: str = Field(
        alias="local-addr-type", default="dynamic", description="local addr type."
    )
    nat: StatusEnum = Field(default=StatusEnum.DISABLE, description="nat.")

    remote_subnet: list[str] = Field(
        alias="remote-subnet", default=[DEFAULT_NETWORK], description="action."
    )
    vpn_ipsec_phase1_interface: VpnIpsecPhase1Interface = Field(
        alias="vpn ipsec phase1-interface", description="vpn ipsec phase1-interface."
    )
    vpn_ipsec_phase2_interface: VpnIpsecPhase2Interface | None = Field(
        default=None,
        alias="vpn ipsec phase2-interface",
        description="vpn ipsec phase2-interface.",
    )
    system_interface: SystemInterface = Field(
        alias="system interface", description="system interface."
    )


class FortiManagerIPSecTemplateAction(BaseModel):
    """
    fortimanager ipsec template action
    """

    action: str = Field(default="conf-ipsec-template", description="action.")
    value: FortiManagerUpdateIPSec = Field(..., description="value.")
    seq: int | None = Field(
        default=None,
        description="Represents the unique sequential number of the IPSec configuration.",
    )
