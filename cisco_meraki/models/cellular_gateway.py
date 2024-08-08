"""
Models used in Meraki API requests/responses for Cellular Gateway API.
DISCLAIMER: although they have similar names,
they are different than ReservedIpRanges and FixedIpAssignments of a VLAN.
"""

import ipaddress
from typing import List
from enum import Enum

from pydantic import BaseModel, Field


class ReservedIpRange(BaseModel):
    """
    Reserved range of IP addresses for Cellular Gateways
    """

    start: ipaddress.IPv4Address = Field(
        description="first IPv4 address of the range (included)",
    )
    end: ipaddress.IPv4Address = Field(
        description="Last IPv4 address of the range (included)"
    )
    comment: str | None = Field(
        description="User-friendly comment to describe the IP range",
        default=None,
    )


class FixedIpAssignment(BaseModel):
    """
    Fixed associations between specific devices (identified by their MAC address)
    and an IP address in the network
    """

    name: str | None = Field(
        description="User-friendly name to assign to this IP assignment", default=None
    )
    mac: str = Field(
        description="MAC address of the specific device",
        regex="[0-9a-f]{2}([-:]?[0-9a-f]{2}){5}$",
    )
    ip: ipaddress.IPv4Address = Field(
        description="IPv4 address to assign to the device"
    )


class CellularGatewayLanSettings(BaseModel):
    """Cellular Gateway LAN Settings API model"""

    deviceName: str = Field(description="name of the MG device")
    deviceLanIp: ipaddress.IPv4Network = Field(
        description="Current LAN IP of the device"
    )
    deviceSubnet: str = Field(description="Subnet the device is in")
    fixedIpAssignments: List[FixedIpAssignment] = Field(
        description="Fixed IP Assignment for the MG device", default=[]
    )
    reservedIpRanges: List[ReservedIpRange] = Field(
        description="Reserved IP ranges for the MG device", default=[]
    )


class CellularGatewayLanSettingsUpdateRequest(BaseModel):
    """Cellular Gateway LAN settings update request payload"""

    fixedIpAssignments: List[FixedIpAssignment] = Field(
        description="Fixed IP Assignment for the MG device", default=[]
    )
    reservedIpRanges: List[ReservedIpRange] = Field(
        description="Reserved IP ranges for the MG device", default=[]
    )


class Subnet(BaseModel):
    """
    A subnet defined in the context of the Subnet Pool
    dedicated to a specific cellular gateway device
    """

    serial: str = Field(
        description="serial of the cellular gateway device",
    )
    name: str | None = Field(
        default=None, description="descriptive name for the subnet"
    )
    applianceIp: str = Field(
        description="IP of the gateway in this subnet",
    )
    subnet: str = Field(
        description="CIDR of the dedicated subnet",
    )


class UpdateSubnetPoolData(BaseModel):
    """
    Subnet Pool definition API update request body
    """

    deploymentMode: str | None = None
    cidr: str | None = None
    mask: int | None = None


class SubnetPool(UpdateSubnetPoolData):
    """
    Subnet Pool definition
    """

    subnets: List[Subnet]


class Leasetime(str, Enum):
    """
    Allowed values for lease time
    """

    T_30M = "30 minutes"
    T_1H = "1 hour"
    T_4H = "4 hours"
    T_12H = "12 hours"
    T_1D = "1 day"
    T_1W = "1 week"


class NameserversGroup(str, Enum):
    """
    Allowed values for nameservers_group
    """

    UPSTREAM_DNS = "upstream_dns"
    GOOGLE_DNS = "google_dns"
    OPEN_DNS = "opendns"
    CUSTOM = "custom"


class CellularGatewayDhcp(BaseModel):
    """
    Cellular gateway DHCP settings API response
    """

    dhcpLeaseTime: Leasetime | None = Field(default=None, description="dhcpLeaseTime")
    dnsNameservers: NameserversGroup | None = Field(
        default=None, description="dnsNameservers"
    )
    dnsCustomNameservers: List[str] | None = Field(
        default=None, description="dnsCustomNameservers"
    )
