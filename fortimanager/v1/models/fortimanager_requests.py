"""
FortiManager API Request V1 Pydantic models
"""

from typing import Generic, TypeVar

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T", bound=BaseModel)


class UserCredentials(BaseModel):
    """
    UserCredentials for login
    """

    user: str
    passwd: str


class FortiManagerAPIRequestParameterV1Base(
    GenericModel, Generic[T], allow_population_by_field_name=True
):
    """
    FortiManagerAPIRequestParameterV1Base class for modelling with all the fields
    """

    url: str
    option: str | None = None
    filter: str | list | None = None
    meta_fields: list[str] | None = Field(default=None, alias="meta fields")
    data: T | list[T] | None = None


# pylint: disable-next = too-few-public-methods
class FortiManagerAPIRequestParameterV1(
    FortiManagerAPIRequestParameterV1Base[T], Generic[T]
):
    """
    Extension of FortiManagerAPIRequestParameterV1Base with data of type T
    """

    data: T | None = None


# pylint: disable-next = too-few-public-methods
class FortiManagerAPIRequestParameterV1List(
    FortiManagerAPIRequestParameterV1Base[T], Generic[T]
):
    """
    Extension of FortiManagerAPIRequestParameterV1Base with data of type List[T]
    """

    data: list[T] | None = None


# pylint: disable-next = too-few-public-methods
class FortiManagerAPIRequestParameterV1NoData(
    FortiManagerAPIRequestParameterV1Base[BaseModel]
):
    """
    Extension of FortiManagerAPIRequestParameterV1Base with data of type None
    """

    data: None = None


class FortiManagerAPIRequestV1Base(BaseModel):
    """
    FortiManagerAPIRequestV1Base class for modelling
    FortiManagerAPIRequestV1 base class
    """

    method: str
    session: str | None = None
    verbose: int = 1


class FortiManagerAPIRequestV1(FortiManagerAPIRequestV1Base):
    """
    FortiManagerRequest class for modelling
    FortiManager requests
    """

    params: list[FortiManagerAPIRequestParameterV1Base]
