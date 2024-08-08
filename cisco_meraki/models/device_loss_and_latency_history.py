"""
Device Loss And Latency History pydantic model
"""
from typing import Optional

from pydantic import BaseModel


class DeviceLossAndLatencyHistory(BaseModel):
    """
    Device Loss And Latency History pydantic model
    """

    startTime: Optional[str] = None
    endTime: Optional[str] = None
    lossPercent: Optional[int] = None
    latencyMs: Optional[int] = None
    goodput: Optional[int] = None
    jitter: Optional[int] = None
