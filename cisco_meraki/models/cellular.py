"""
Cellular Models
"""

from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class SimSlot(str, Enum):
    """
    Slot identifier for a sim in a cellular
    """

    SIM1 = "sim1"
    SIM2 = "sim2"


class IpType(str, Enum):
    """
    Supported IP types
    """

    IPV4 = "ipv4"
    IPV6 = "ipv6"


class SimAuthType(str, Enum):
    """
    Supported authentication modes for a Sim
    """

    PAP = "pap"
    CHAP = "chap"
    NONE = "none"


# pylint: disable=line-too-long
class SimAuthentication(BaseModel):
    """
    Credentials set for Sim authentication
    """

    type: SimAuthType | None = Field(
        default=None,
        description="""
    PAP (Password Authentication Protocol) and CHAP (Challenge Handshake Authentication Protocol) are authentication methods used in APN (Access Point Name) for secure network access.
    1) pap sends username and password directly to the server, while CHAP uses challenge-response authentication for enhanced security.
    2) chap is more secure as it avoids transmitting the password directly over the network.
    3) none does not require any authentication
    """,
    )
    username: str | None = Field(
        default=None, description="APN username, if type is set."
    )
    password: str | None = Field(
        default=None,
        description="APN password, if type is set."
        + " (if APN password is not supplied, the password is left unchanged)",
    )


class SimApn(BaseModel):
    """
    Access point name for Sim
    """

    name: str | None = Field(default=None, description="APN name.")
    allowedIpTypes: List[IpType] | None = Field(
        default=None,
        description="Supported IP versions by an APN (Access Point Name). This parameter specifies which versions of the Internet Protocol (IPv4 or IPv6) are enabled for data connectivity through the APN.",
    )
    authentication: SimAuthentication | None = Field(
        default=None,
        description="Enables devices to connect to a mobile network through a specific access point. It requires the use of correct authentication information, such as username and password, to establish a secure connection and grant access to the network.",
    )


# pylint: enable=line-too-long


class CellularSimcard(BaseModel):
    """
    Simcard configuration in the context of a Cellular
    """

    slot: SimSlot | None = None
    isPrimary: bool | None = None
    apns: List[SimApn] | None = None


class SimFailover(BaseModel):
    """
    Whether failover is enabled or not for a Sim
    """

    enabled: bool


class CellularSimcardList(BaseModel):
    """
    Simcards allocation for a Cellular
    """

    sims: List[CellularSimcard] | None = None
    simFailover: SimFailover | None = None
