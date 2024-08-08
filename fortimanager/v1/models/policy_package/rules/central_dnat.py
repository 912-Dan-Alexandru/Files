"""
Fortimanager central DNAT rule model
"""

from pydantic import BaseModel, Field


class FortiManagerCentralDnatV1(BaseModel):
    """
    Central DNAT
    """

    name: list[str] = Field(
        ...,
        description="contains the names of the virtual "
        "IPs connected to the nat central",
    )
