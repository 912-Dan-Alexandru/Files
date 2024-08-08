"""
FortiManager DeviceGroup V1 Pydantic models
"""


from pydantic import BaseModel, Field


class ObjectMemberItem(BaseModel):
    """
    Device name for object member
    """

    name: str
    vdom: str


class FortiManagerDeviceGroupV1(BaseModel):
    """
    FortiManager Device Group V1 model
    """

    oid: int
    name: str
    type: str
    os_type: str
    desc: str
    id: str | None
    cluster_type: str
    object_member: list[ObjectMemberItem] | None = Field(None, alias="object member")
