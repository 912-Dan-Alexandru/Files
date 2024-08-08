"""
Fortinet Template Groups model/models
"""
from enum import Enum

from pydantic import BaseModel, Field


class TemplateGroupType(str, Enum):
    """
    Types of template groups
    """

    TEMPLATE_GROUP = "tmplgrp"


class TemplateGroupSetting(BaseModel):
    """
    Template group settings
    """

    cliprofs: list | None = Field(default=[])
    description: str | None
    fspprofs: list | None = Field(default=[])
    fxtprofs: list | None = Field(default=[])
    templates: list[str] | None = Field(default=[])
    wtpprofs: list | None = Field(default=[])


class TemplateGroup(BaseModel):
    """
    Template group model
    """

    name: str
    oid: int | None
    scope_member: list[str] | None = Field(alias="scope member", default=[])
    template_group_setting: TemplateGroupSetting | None = Field(
        ..., alias="template group setting"
    )
    type: TemplateGroupType = TemplateGroupType.TEMPLATE_GROUP


class TemplateScopeMember(BaseModel):
    """
    A scope member of template groups (device or device group)
    to which the template groups is applied
    """

    name: str
    vdom: str = "root"
