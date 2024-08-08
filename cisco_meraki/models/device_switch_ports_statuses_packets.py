"""
Device Switch Ports Statuses Packets pydantic model
"""
from typing import List, Optional

from pydantic import BaseModel


class RatePersec(BaseModel):
    """
    Rate Persec pydantic model
    """

    total: Optional[int] = None
    sent: Optional[int] = None
    recv: Optional[int] = None


class Packets(BaseModel):
    """
    Packets pydantic model
    """

    desc: Optional[str] = None
    total: Optional[int] = None
    sent: Optional[int] = None
    recv: Optional[int] = None
    ratePersec: Optional[RatePersec] = None


class DeviceSwitchPortsStatusesPackets(BaseModel):
    """
    Device Switch Ports Statuses Packets pydantic model
    """

    portId: Optional[str] = None
    packets: Optional[List[Packets]] = None
