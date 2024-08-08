"""
Fortimanager IPv6 central DNAT rule model
"""

from pydantic import BaseModel, Field


class FortiManagerCentralDnat6V1(BaseModel):
    """
    Configure DNAT IPv6
    """

    name: list[str] = Field(
        ...,
        description="Contains the names of the IPv6 virtual"
        " IPs connected to the NAT central.",
    )
