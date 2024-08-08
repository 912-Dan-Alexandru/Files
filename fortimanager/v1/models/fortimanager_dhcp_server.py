"""
FortiManager DHCP Server V1 Pydantic models
"""

from enum import Enum

from pydantic import BaseModel, Field

# pylint: disable=line-too-long
# ruff: noqa: S104


class OptionTypeEnum(str, Enum):
    """
    Enum representing DHCP option types.
    """

    HEX = "hex"  # 0
    STRING = "string"  # 1
    IP = "ip"  # 2
    FQDN = "fqdn"  # 3


class ActionEnum(str, Enum):
    """
    Enum representing DHCP actions.
    """

    ASSIGN = "assign"  # 0
    BLOCK = "block"  # 1
    RESERVED = "reserved"  # 2


class IdTypeEnum(str, Enum):
    """
    Enum representing identifier types.
    """

    HEX = "hex"  # 0
    STRING = "string"  # 1


class TypeEnum(str, Enum):
    """
    Enum representing DHCP types.
    """

    MAC = "mac"  # 1
    OPTION82 = "option82"  # 2


class DdnsAuthEnum(str, Enum):
    """
    Enum representing DDNS authentication modes.
    """

    DISABLE = "disable"  # 0
    TSIG = "tsig"  # 7


class ServiceEnum(str, Enum):
    """
    Enum representing DHCP service options.
    """

    DEFAULT = "default"  # 3
    SPECIFY = "specify"  # 5
    LOCAL = "local"  # 21


class IpModeEnum(str, Enum):
    """
    Enum representing DHCP IP assignment modes.
    """

    RANGE = "range"  # 0
    USRGRP = "usrgrp"  # 1


class MacAclDefaultActionEnum(str, Enum):
    """
    Enum representing MAC ACL default actions.
    """

    ASSIGN = "assign"  # 0
    BLOCK = "block"  # 1


class ServerTypeEnum(str, Enum):
    """
    Enum representing DHCP server types.
    """

    REGULAR = "regular"  # 1
    IPSEC = "ipsec"  # 31


class StatusEnum(str, Enum):
    """
    Enum representing status options.
    """

    DISABLE = "disable"  # 0
    ENABLE = "enable"  # 1


class TimezoneEnum(str, Enum):
    """
    Enum representing timezones.
    """

    TZ_00 = "00"  # 0
    TZ_01 = "01"  # 1
    TZ_02 = "02"  # 2
    TZ_03 = "03"  # 3
    TZ_04 = "04"  # 4
    TZ_05 = "05"  # 5
    TZ_06 = "06"  # 6
    TZ_07 = "07"  # 7
    TZ_08 = "08"  # 8
    TZ_09 = "09"  # 9
    TZ_10 = "10"  # 10
    TZ_11 = "11"  # 11
    TZ_12 = "12"  # 12
    TZ_13 = "13"  # 13
    TZ_14 = "14"  # 14
    TZ_15 = "15"  # 15
    TZ_16 = "16"  # 16
    TZ_17 = "17"  # 17
    TZ_18 = "18"  # 18
    TZ_19 = "19"  # 19
    TZ_20 = "20"  # 20
    TZ_21 = "21"  # 21
    TZ_22 = "22"  # 22
    TZ_23 = "23"  # 23
    TZ_24 = "24"  # 24
    TZ_25 = "25"  # 25
    TZ_26 = "26"  # 26
    TZ_27 = "27"  # 27
    TZ_28 = "28"  # 28
    TZ_29 = "29"  # 29
    TZ_30 = "30"  # 30
    TZ_31 = "31"  # 31
    TZ_32 = "32"  # 32
    TZ_33 = "33"  # 33
    TZ_34 = "34"  # 34
    TZ_35 = "35"  # 35
    TZ_36 = "36"  # 36
    TZ_37 = "37"  # 37
    TZ_38 = "38"  # 38
    TZ_39 = "39"  # 39
    TZ_40 = "40"  # 40
    TZ_41 = "41"  # 41
    TZ_42 = "42"  # 42
    TZ_43 = "43"  # 43
    TZ_44 = "44"  # 44
    TZ_45 = "45"  # 45
    TZ_46 = "46"  # 46
    TZ_47 = "47"  # 47
    TZ_48 = "48"  # 48
    TZ_49 = "49"  # 49
    TZ_50 = "50"  # 50
    TZ_51 = "51"  # 51
    TZ_52 = "52"  # 52
    TZ_53 = "53"  # 53
    TZ_54 = "54"  # 54
    TZ_55 = "55"  # 55
    TZ_56 = "56"  # 56
    TZ_57 = "57"  # 57
    TZ_58 = "58"  # 58
    TZ_59 = "59"  # 59
    TZ_60 = "60"  # 60
    TZ_61 = "61"  # 61
    TZ_62 = "62"  # 62
    TZ_63 = "63"  # 63
    TZ_64 = "64"  # 64
    TZ_65 = "65"  # 65
    TZ_66 = "66"  # 66
    TZ_67 = "67"  # 67
    TZ_68 = "68"  # 68
    TZ_69 = "69"  # 69
    TZ_70 = "70"  # 70
    TZ_71 = "71"  # 71
    TZ_72 = "72"  # 72
    TZ_73 = "73"  # 73
    TZ_74 = "74"  # 74
    TZ_75 = "75"  # 75
    TZ_76 = "76"  # 76
    TZ_77 = "77"  # 77
    TZ_78 = "78"  # 78
    TZ_79 = "79"  # 79
    TZ_80 = "80"  # 80
    TZ_81 = "81"  # 81
    TZ_82 = "82"  # 82
    TZ_83 = "83"  # 83
    TZ_84 = "84"  # 84
    TZ_85 = "85"  # 85
    TZ_86 = "86"  # 86
    TZ_87 = "87"  # 87


class TimezoneOptionEnum(str, Enum):
    """
    Enum representing DHCP timezone options.
    """

    DISABLE = "disable"  # 0
    DEFAULT = "default"  # 3
    SPECIFY = "specify"  # 5


class WifiAcServiceEnum(str, Enum):
    """
    Enum representing WiFi AC service options.
    """

    SPECIFY = "specify"  # 5
    LOCAL = "local"  # 21


class DhcpExcludeRange(BaseModel, allow_population_by_field_name=True):
    """
    Exclude one or more ranges of IP addresses from being assigned to clients.
    """

    end_ip: str = Field(
        alias="end-ip", default="0.0.0.0", description="End of IP range."
    )
    id: int = Field(default=0, description="ID.", le=4294967295)
    start_ip: str = Field(
        alias="start-ip", default="0.0.0.0", description="Start of IP range."
    )


class DhcpIpRange(BaseModel, allow_population_by_field_name=True):
    """
    DHCP IP range configuration.
    """

    end_ip: str = Field(
        alias="end-ip", default="0.0.0.0", description="End of IP range."
    )
    id: int = Field(default=0, description="ID.", le=4294967295)
    start_ip: str = Field(
        alias="start-ip", default="0.0.0.0", description="Start of IP range."
    )
    oid: int = Field(default=2096, description="oid.")
    lease_time: int = Field(default=0, alias="lease-time", description="Leasetime.")
    uci_match: str = Field(default=None, alias="uci-match", description="Uci match.")
    uci_string: str | list[str] = Field(
        default=None, alias="uci-string", description="Uci string."
    )
    vci_match: str = Field(default=None, alias="vci-match", description="Vci match.")
    vci_string: str | list[str] | None = Field(
        default=None, alias="vci-string", description="Vci string."
    )


class DhcpOptions(BaseModel):
    """
    DHCP options.
    """

    id: int = Field(default=0, description="ID.", le=4294967295)
    type: OptionTypeEnum = Field(
        default=OptionTypeEnum.HEX, description="DHCP option type."
    )
    value: str = Field(description="DHCP option value.", max_length=312)
    ip: list[str] = Field(..., description="DHCP option IPs.")
    code: int = Field(default=0, description="DHCP option code.", le=255)


class DhcpReservedAddress(BaseModel, allow_population_by_field_name=True):
    """
    Options for the DHCP server to assign IP settings to specific MAC addresses.
    """

    id: int = Field(default=0, description="ID.", le=4294967295)
    type: TypeEnum = Field(
        default=TypeEnum.MAC, description="DHCP reserved-address type."
    )
    description: str = Field(description="Description.", max_length=255)
    # Match Criteria
    mac: str = Field(
        default="00:00:00:00:00:00",
        description="MAC address of the client that will get the reserved IP address.",
    )
    circuit_id_type: IdTypeEnum = Field(
        alias="circuit-id-type",
        default=IdTypeEnum.STRING,
        description="DHCP option circuit id type.",
    )
    circuit_id: str = Field(
        alias="circuit-id",
        description="Option 82 circuit-ID of the client that will get the reserved IP address.",
        max_length=312,
    )
    remote_id_type: IdTypeEnum = Field(
        alias="remote-id-type",
        default=IdTypeEnum.STRING,
        description="DHCP option remote id type.",
    )
    remote_id: str = Field(
        alias="remote-id",
        description="Option 82 remote-ID of the client that will get the reserved IP address.",
        max_length=312,
    )
    # Action
    action: ActionEnum = Field(
        default=ActionEnum.RESERVED,
        description="Options for the DHCP server to configure the client with the reserved MAC address.",
    )
    ip: str = Field(
        default="0.0.0.0", description="IP address to be reserved for the MAC address."
    )


class FortiManagerDHCPServerV1(BaseModel, allow_population_by_field_name=True):
    """
    Configure DHCP servers.
    """

    id: int = Field(default=0, description="ID.", le=4294967295)
    interface: str | list[str] = Field(
        ...,
        description="DHCP server can assign IP configurations to clients connected to this interface.",
    )
    # DHCP Status
    status: StatusEnum = Field(
        default=StatusEnum.ENABLE, description="Enable/disable this DHCP configuration."
    )
    # Address Range
    ip_range: list[DhcpIpRange] = Field(
        alias="ip-range", default=None, description="DHCP IP range configuration."
    )
    # Netmask
    netmask: str = Field(
        default="0.0.0.0", description="Netmask assigned by the DHCP server."
    )
    # Default Gateway
    default_gateway: str = Field(
        alias="default-gateway",
        default="0.0.0.0",
        description="Default gateway IP address assigned by the DHCP server.",
    )
    # DNS Server
    dns_service: ServiceEnum = Field(
        alias="dns-service",
        default=ServiceEnum.SPECIFY,
        description="Options for assigning DNS servers to DHCP clients.",
    )
    dns_server1: str = Field(
        alias="dns-server1", default="0.0.0.0", description="DNS server 1."
    )
    dns_server2: str = Field(
        alias="dns-server2", default="0.0.0.0", description="DNS server 2."
    )
    dns_server3: str = Field(
        alias="dns-server3", default="0.0.0.0", description="DNS server 3."
    )
    dns_server4: str = Field(
        alias="dns-server4", default="0.0.0.0", description="DNS server 4."
    )
    # Lease Time
    lease_time: int = Field(
        alias="lease-time",
        default=604800,
        description="Lease time in seconds, 0 means unlimited.",
        le=8640000,
    )
    # ADVANCED
    server_type: ServerTypeEnum = Field(
        alias="server-type",
        default=ServerTypeEnum.REGULAR,
        description="DHCP server can be a normal DHCP server or an IPsec DHCP server.",
    )
    # NTP Server
    ntp_service: ServiceEnum = Field(
        alias="ntp-service",
        default=ServiceEnum.SPECIFY,
        description="Options for assigning Network Time Protocol (NTP) servers to DHCP clients.",
    )
    ntp_server1: str = Field(
        alias="ntp-server1", default="0.0.0.0", description="NTP server 1."
    )
    ntp_server2: str = Field(
        alias="ntp-server2", default="0.0.0.0", description="NTP server 2."
    )
    ntp_server3: str = Field(
        alias="ntp-server3", default="0.0.0.0", description="NTP server 3."
    )
    # Wireless Controller
    wifi_ac_service: WifiAcServiceEnum = Field(
        alias="wifi-ac-service",
        default=WifiAcServiceEnum.SPECIFY,
        description="Options for assigning WiFi access controllers to DHCP clients.",
    )
    wifi_ac1: str = Field(
        alias="wifi-ac1",
        default="0.0.0.0",
        description="WiFi Access Controller 1 IP address (DHCP option 138, RFC 5417).",
    )
    wifi_ac2: str = Field(
        alias="wifi-ac2",
        default="0.0.0.0",
        description="WiFi Access Controller 2 IP address (DHCP option 138, RFC 5417).",
    )
    wifi_ac3: str = Field(
        alias="wifi-ac3",
        default="0.0.0.0",
        description="WiFi Access Controller 3 IP address (DHCP option 138, RFC 5417).",
    )
    # Timezone option
    timezone_option: TimezoneOptionEnum = Field(
        alias="timezone-option",
        default=TimezoneOptionEnum.DISABLE,
        description="Options for the DHCP server to set the client's time zone.",
    )
    timezone: TimezoneEnum = Field(
        default=TimezoneEnum.TZ_00,
        description="Select the time zone to be assigned to DHCP clients.",
    )
    # Next Bootstrap Server
    next_server: str = Field(
        alias="next-server",
        default="0.0.0.0",
        description="IP address of a server (for example, a TFTP sever) that DHCP clients can download a boot file from.",
    )
    # TFTP Server(s)
    tftp_server: list[str] = Field(
        alias="tftp-server",
        description="One or more hostnames or IP addresses of the TFTP servers in quotes separated by spaces.",
    )
    # Additional DHCP Options
    options: list[DhcpOptions] = Field(default=None, description="DHCP options.")
    # IP Address Assignment Rules
    reserved_address: list[DhcpReservedAddress] = Field(
        alias="reserved-address",
        default=None,
        description="Options for the DHCP server to assign IP settings to specific MAC addresses.",
    )
    # Others
    conflicted_ip_timeout: int = Field(
        alias="conflicted-ip-timeout",
        default=1800,
        description="Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused.",
        le=8640000,
        ge=60,
    )
    ip_mode: IpModeEnum = Field(
        alias="ip-mode",
        default=IpModeEnum.RANGE,
        description="Method used to assign client IP.",
    )
    exclude_range: DhcpExcludeRange = Field(
        alias="exclude-range",
        default=None,
        description="Exclude one or more ranges of IP addresses from being assigned to clients.",
    )
    ddns_zone: str = Field(
        default=None,
        alias="ddns-zone",
        description="Zone of your domain name (ex. DDNS.com).",
        max_length=64,
    )
    domain: str = Field(
        default=None,
        description="Domain name suffix for the IP addresses that the DHCP server assigns to clients.",
        max_length=35,
    )
    filename: str = Field(
        default=None,
        description="Name of the boot file on the TFTP server.",
        max_length=127,
    )
    auto_configuration: StatusEnum = Field(
        alias="auto-configuration",
        default=StatusEnum.ENABLE,
        description="Enable/disable auto configuration.",
    )
    auto_managed_status: StatusEnum = Field(
        alias="auto-managed-status",
        default=StatusEnum.ENABLE,
        description="Enable/disable use of this DHCP server once this interface has been assigned an IP address from FortiIPAM.",
    )
    ddns_auth: DdnsAuthEnum = Field(
        alias="ddns-auth",
        default=DdnsAuthEnum.DISABLE,
        description="DDNS authentication mode.",
    )
    ddns_key: str = Field(
        alias="ddns-key",
        default="ENC DCPzbLQGi6k8KzKQnSU6dgRtH2o3UokYCY9exMISw/6nSTIs4Gq3jO0RoueHbvLpBnJgzrrTmkGB/2TOYE5sb6XlZAkN4WpKMXI6BmFGYvuOjb072o1T6m6/aVA=",
        description="DDNS update key (base 64 encoding).",
    )
    ddns_keyname: str = Field(
        default=None,
        alias="ddns-keyname",
        description="DDNS update key name.",
        max_length=64,
    )
    ddns_server_ip: str = Field(
        alias="ddns-server-ip", default="0.0.0.0", description="DDNS server IP."
    )
    ddns_ttl: int = Field(
        alias="ddns-ttl", default=300, description="TTL.", le=86400, ge=60
    )
    ddns_update: StatusEnum = Field(
        alias="ddns-update",
        default=StatusEnum.DISABLE,
        description="Enable/disable DDNS update for DHCP.",
    )
    ddns_update_override: StatusEnum = Field(
        alias="ddns-update-override",
        default=StatusEnum.DISABLE,
        description="Enable/disable DDNS update override for DHCP.",
    )
    dhcp_settings_from_fortiipam: StatusEnum = Field(
        alias="dhcp-settings-from-fortiipam",
        default=StatusEnum.DISABLE,
        description="Enable/disable populating of DHCP server settings from FortiIPAM.",
    )
    forticlient_on_net_status: StatusEnum = Field(
        alias="forticlient-on-net-status",
        default=StatusEnum.ENABLE,
        description="Enable/disable FortiClient-On-Net service for this DHCP server.",
    )
    ipsec_lease_hold: int = Field(
        alias="ipsec-lease-hold",
        default=60,
        description="DHCP over IPsec leases expire this many seconds after tunnel down (0 to disable forced-expiry).",
        le=8640000,
    )
    mac_acl_default_action: MacAclDefaultActionEnum = Field(
        alias="mac-acl-default-action",
        default=MacAclDefaultActionEnum.ASSIGN,
        description="MAC access control default action (allow or block assigning IP settings).",
    )
    vci_match: StatusEnum = Field(
        alias="vci-match",
        default=StatusEnum.DISABLE,
        description="Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served.",
    )
    vci_string: list[str] = Field(
        default=None,
        alias="vci-string",
        description="One or more VCI strings in quotes separated by spaces.",
    )
    wins_server1: str = Field(
        alias="wins-server1", default="0.0.0.0", description="WINS server 1."
    )
    wins_server2: str = Field(
        alias="wins-server2", default="0.0.0.0", description="WINS server 2."
    )


class CreateFortiManagerDHCPServerV1(BaseModel, allow_population_by_field_name=True):
    """
    FortiManager DHCP V1 model
    """

    interface: str | list[str] | None = None
    status: StatusEnum | None = None
    ip_range: list[DhcpIpRange] | None = Field(default=None, alias="ip-range")
    netmask: str | None = None
    default_gateway: str | None = Field(default=None, alias="default-gateway")
    dns_service: ServiceEnum | None = Field(default=None, alias="dns-service")
    dns_server1: str | None = Field(default=None, alias="dns-server1")
    dns_server2: str | None = Field(default=None, alias="dns-server2")
    dns_server3: str | None = Field(default=None, alias="dns-server3")
    dns_server4: str | None = Field(default=None, alias="dns-server4")
    lease_time: int | None = Field(default=None, alias="lease-time")
    server_type: ServerTypeEnum | None = Field(default=None, alias="server-type")
    ntp_service: ServiceEnum | None = Field(default=None, alias="ntp-service")
    ntp_server1: str | None = Field(default=None, alias="ntp-server1")
    ntp_server2: str | None = Field(default=None, alias="ntp-server2")
    ntp_server3: str | None = Field(default=None, alias="ntp-server3")
    wifi_ac_service: WifiAcServiceEnum | None = Field(
        default=None, alias="wifi-ac-service"
    )
    wifi_ac1: str | None = Field(default=None, alias="wifi-ac1")
    wifi_ac2: str | None = Field(default=None, alias="wifi-ac2")
    wifi_ac3: str | None = Field(default=None, alias="wifi-ac3")
    timezone_option: TimezoneOptionEnum | None = Field(
        default=None, alias="timezone-option"
    )
    timezone: TimezoneEnum | None = None
    next_server: str | None = Field(default=None, alias="next-server")
    tftp_server: list[str] | None = Field(default=None, alias="tftp-server")
    options: list[DhcpOptions] | None = None
    reserved_address: list[DhcpReservedAddress] | None = Field(
        default=None, alias="reserved-address"
    )


# pylint: enable=line-too-long


class UpdateFortiManagerDHCPServerV1(CreateFortiManagerDHCPServerV1):
    """
    Update FortiManager DHCP V1 model
    """
