"""
FortiManager DNS V1 Pydantic models
"""
# pylint: disable=line-too-long

from enum import Enum

from pydantic import BaseModel, Field

from .metaclass import AllOptionalMeta


class StatusEnum(str, Enum):
    """
    Enum representing Status option.
    """

    DISABLE = "disable"  # 0
    ENABLE = "enable"  # 1


class InterfaceSelectMethodEnum(str, Enum):
    """
    Enum representing Interface Select Method types.
    """

    AUTO = "auto"  # 0
    SDWAN = "sdwan"  # 1
    SPECIFY = "specify"  # 2


class LogEnum(str, Enum):
    """
    Enum representing Log types.
    """

    DISABLE = "disable"  # 0
    ERROR = "error"  # 1
    ALL = "all"  # 2


class ProtocolEnum(str, Enum):
    """
    Enum representing Protocol types.
    """

    CLEARTEXT = "cleartext"  # 1
    DOT = "dot"  # 2
    DOH = "doh"  # 4


class ServerSelectMethodEnum(str, Enum):
    """
    Enum representing Server Select Method option.
    """

    LEAST_RTT = "least-rtt"  # 1
    FAILOVER = "failover"  # 2


class FortiManagerDeviceSystemDnsV1(BaseModel):
    """
    Device system global DNS model
    """

    alt_primary: str = Field(
        alias="alt-primary",
        default="0.0.0.0",  # noqa: S104
        description="Alternate primary DNS server. This is not used as a failover DNS server.",
    )
    alt_secondary: str = Field(
        alias="alt-secondary",
        default="0.0.0.0",  # noqa: S104
        description="Alternate secondary DNS server. This is not used as a failover DNS server.",
    )
    cache_notfound_responses: StatusEnum = Field(
        alias="cache-notfound-responses",
        default=StatusEnum.DISABLE,
        description="Enable/disable response from the DNS server when a record is not in cache.",
    )
    dns_cache_limit: int = Field(
        alias="dns-cache-limit",
        default=5000,
        description="Maximum number of records in the DNS cache.",
        ge=0,
        le=4294967295,
    )
    dns_cache_ttl: int = Field(
        alias="dns-cache-ttl",
        default=1800,
        description="Duration in seconds that the DNS cache retains information.",
        le=86400,
        ge=60,
    )
    domain: list[str] = Field(
        description="Search suffix list for hostname lookup.",
        default=[],
    )
    interface: str | list[str] = Field(
        description="Specify outgoing interface to reach server.",
        default=[],
    )
    interface_select_method: InterfaceSelectMethodEnum = Field(
        alias="interface-select-method",
        default=InterfaceSelectMethodEnum.AUTO,
        description="Specify how to select outgoing interface to reach server.",
    )
    ip6_primary: str = Field(
        alias="ip6-primary",
        default="::",
        description="Primary DNS server IPv6 address.",
    )
    ip6_secondary: str = Field(
        alias="ip6-secondary",
        default="::",
        description="Secondary DNS server IPv6 address.",
    )
    log: LogEnum = Field(default=LogEnum.DISABLE, description="Local DNS log setting.")
    primary: str = Field(
        default="0.0.0.0",  # noqa: S104
        description="Primary DNS server IP address.",
    )
    protocol: ProtocolEnum | list[ProtocolEnum] = Field(
        default=ProtocolEnum.CLEARTEXT, description="DNS transport protocols."
    )
    retry: int = Field(
        default=2,
        description="Number of times to retry (0 - 5).",
        ge=0,
        le=5,
    )
    secondary: str = Field(
        default="0.0.0.0",  # noqa: S104
        description="Secondary DNS server IP address.",
    )
    server_hostname: list[str] = Field(
        default=[], alias="server-hostname", description="DNS server host name list."
    )
    server_select_method: ServerSelectMethodEnum = Field(
        alias="server-select-method",
        default=ServerSelectMethodEnum.LEAST_RTT,
        description="Specify how configured servers are prioritized.",
    )
    source_ip: str = Field(
        alias="source-ip",
        default="0.0.0.0",  # noqa: S104
        description="IP address used by the DNS server as its source IP.",
    )
    ssl_certificate: str | list[str] = Field(
        alias="ssl-certificate",
        default="Fortinet_Factory",
        description="Name of local certificate for SSL connections.",
    )
    timeout: int = Field(
        default=5,
        description="DNS query timeout interval in seconds (1 - 10).",
        le=10,
        ge=1,
    )

    fqdn_cache_ttl: str | None = Field(alias="fqdn-cache-ttl", default=None)
    fqdn_max_refresh: str | None = Field(alias="fqdn-max-refresh", default=None)
    fqdn_min_refresh: str | None = Field(alias="fqdn-min-refresh", default=None)


class FortiManagerModifyDeviceSystemDnsV1(
    FortiManagerDeviceSystemDnsV1, metaclass=AllOptionalMeta
):
    """
    Device system global DNS model with all fields optional
    """


# pylint: enable=line-too-long
