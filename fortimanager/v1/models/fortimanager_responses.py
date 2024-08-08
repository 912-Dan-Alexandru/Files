"""
FortiManager API Response V1 Pydantic models
"""

from pydantic import BaseModel


class Status(BaseModel):
    """
    status response
    """

    code: int
    message: str


class ResultItem(BaseModel):
    """
    result response
    """

    data: list[dict] | dict | None
    status: Status
    url: str


class FortiManagerAPIResponseStatusV1(BaseModel):
    """
    FortiManagerRequest class for modelling
    FortiManager response status
    """

    result: list[ResultItem]
    id: int | None = None


class FortiManagerAPIResponseStatusWithSessionV1(FortiManagerAPIResponseStatusV1):
    """
    FortiManagerRequest class for modelling
    FortiManager response status for login endpoint
    """

    session: int | str | None
