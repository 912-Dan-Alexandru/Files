"""
Wrapper of VeloEvetV1Data and VeloEventV2Data
"""

from pydantic import BaseModel

from common.southbound.velocloud.v1.models.event import VeloEventV1Data
from common.southbound.velocloud.v2.models.event import VeloEventV2Data


class VeloEventData(BaseModel):
    """
    Wrapper of VeloEventV1Data and VeloEventV2Data
    """

    event_data: VeloEventV1Data | VeloEventV2Data
