"""
Velocloud V2 Event
"""

from typing import List

from pydantic import BaseModel


class VeloEventV1Data(BaseModel):
    """
    Velocloud Event Data
    """

    id: int
    event: str
    eventTime: str
    category: str
    severity: str
    message: str
    detail: str | None = None
    enterpriseUserName: str | None = None
    edgeName: str | None = None
    segmentName: str | None = None


class VeloEventV1MetaData(BaseModel):
    """
    Velocloud Event Metadata
    """

    limit: int
    more: bool
    nextPageLink: str | None = None
    prevPageLink: str | None = None


class VeloEventV1(BaseModel):
    """
    Velocloud Event
    """

    _href: str | None = None
    data: List[VeloEventV1Data] | None = None
    metaData: VeloEventV1MetaData | None = None
    data_count: int | None = None
