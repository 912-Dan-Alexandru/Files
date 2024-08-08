"""
Fortimanager central SNAT rule model
"""

# pylint: disable=line-too-long, too-many-lines
from enum import Enum

from pydantic import BaseModel, Field

from common.southbound.fortimanager.v1.models.policy_package.rules.common.enums import (
    StatusEnum,
)


class TypeEnum(Enum):
    """
    IP type
    """

    IPV4 = "ipv4"  # 7
    IPV6 = "ipv6"  # 8


class FortiManagerCentralSnatV1(BaseModel):
    """
    Configure IPv4 and IPv6 central SNAT policies.
    """

    comments: str = Field(..., description="Comment.", max_length=1023)
    dst_addr: list[str] = Field(
        ..., alias="dst-addr", description="IPv4 Destination address."
    )
    dst_addr6: list[str] = Field(
        ..., alias="dst-addr6", description="IPv6 Destination address."
    )
    dst_port: str = Field(
        alias="dst-port",
        default="0",
        description="Destination port or port range (1 to 65535, 0 means any port).",
    )
    dstintf: list[str] = Field(
        ..., description="Destination interface name from available interfaces."
    )
    nat: StatusEnum = Field(
        default=StatusEnum.ENABLE, description="Enable/disable source NAT."
    )
    nat_ippool: list[str] = Field(
        ...,
        alias="nat-ippool",
        description="Name of the IP pools to be used to translate addresses from available IP Pools.",
    )
    nat_ippool6: list[str] = Field(
        ..., alias="nat-ippool6", description="IPv6 pools to be used for source NAT."
    )
    nat_port: str = Field(
        alias="nat-port",
        default="0",
        description="Translated port or port range (1 to 65535, 0 means any port).",
    )
    nat46: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable NAT46."
    )
    nat64: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable NAT64."
    )
    orig_addr: list[str] = Field(
        ..., alias="orig-addr", description="IPv4 Original address."
    )
    orig_addr6: list[str] = Field(
        ..., alias="orig-addr6", description="IPv6 Original address."
    )
    orig_port: str = Field(
        alias="orig-port",
        default="0",
        description="Original TCP port (1 to 65535, 0 means any port).",
    )
    policyid: int = Field(default=0, description="Policy ID.", le=4294967295)
    protocol: int = Field(
        default=0, description="Integer value for the protocol type (0 - 255).", le=255
    )
    srcintf: list[str] = Field(
        ..., description="Source interface name from available interfaces."
    )
    status: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        description="Enable/disable the active status of this policy.",
    )
    type: TypeEnum = Field(default=TypeEnum.IPV4, description="IPv4/IPv6 source NAT.")
    uuid: str = Field(
        default="00000000-0000-0000-0000-000000000000",
        description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).",
    )
