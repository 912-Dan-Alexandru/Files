"""
FortiManager ADOM V1 Pydantic models
"""


from pydantic import BaseModel, Field, validator


class ObjectMemberItem(BaseModel):
    """
    Object Member model
    """

    name: str
    vdom: str | None


class AdomMetaFields(BaseModel):
    """
    FortiManager ADOM Meta fields
    """

    acctv: str | None = Field(None, alias="ACCTV")
    vf_opco_name: str | None = Field(None, alias="VF OpCo Name")
    vf_customer_id: str | None = Field(None, alias="VF Customer ID")
    vf_SDWAN_service_provided: str | None = Field(
        None, alias="VF SDWAN Service Provided"
    )


class FortiManagerADOMV1Base(BaseModel):
    """
    FortiManager base ADOM V1 model
    """

    create_time: int | None = None
    desc: str | None = None
    flags: str | None | list[str] = None
    mig_mr: int | None = None
    mig_os_ver: str | None = None
    mode: str | None = None
    mr: int | None = Field(default=None, description="minor version number")
    name: str
    obj_customize: str | None = None
    os_ver: int | None = Field(default=None, description="major version number")

    @validator("os_ver", pre=True, allow_reuse=True)
    @classmethod
    def convert_os_ver(cls, v):
        """
        Method for converting string "7.0" to integer 7
        The pydantic validator must have cls as first argument not self
        So ignore if sonar says it is a code smell
        """
        str_ver = str(v).split(".", maxsplit=1)[0]
        try:
            return int(str_ver)
        except ValueError:
            return 0

    restricted_prds: str | None = None
    state: int | None = None
    tab_status: str | None = None
    workspace_mode: int | None = None
    object_member: list[ObjectMemberItem] | None = Field(
        default=None, alias="object member"
    )
    meta_fields: AdomMetaFields | None = Field(default=None, alias="meta fields")
    tz: int = Field(default=-1, description="Timezone, -1 is server default")


class FortiManagerADOMV1(FortiManagerADOMV1Base):
    """
    FortiManager ADOM V1 model

    """

    oid: int | None = None
    uuid: str | None = Field(default=None, description="Unique ID")


class CreateFortiManagerADOMV1(BaseModel):
    """
    FortiManager ADOM V1 model
    """

    desc: str | None = None
    flags: str | None | list[str] = None
    name: str
    meta_fields: AdomMetaFields | None = Field(default=None, alias="meta fields")
    tz: int = Field(default=-1, description="Timezone, -1 is server default")


class UpdateFortiManagerADOMV1(FortiManagerADOMV1Base):
    """
    FortiManager Update ADOM V1 model
    """
