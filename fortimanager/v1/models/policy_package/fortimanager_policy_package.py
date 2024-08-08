"""
Fortinet policy package models
"""

from __future__ import annotations
from enum import Enum

from pydantic import BaseModel, Field

DISABLE = "disable"
ENABLE = "enable"


# pylint: disable=line-too-long
class Type(str, Enum):
    """
    Policy type
    """

    PKG = "pkg"
    FOLDER = "folder"


class CentralNat(str, Enum):
    """
    Central NAT
    """

    DISABLE = DISABLE
    ENABLE = ENABLE


class ConsolidatedFirewallMode(str, Enum):
    """
    Consolidated firewall mode
    """

    DISABLE = DISABLE
    ENABLE = ENABLE


class FwpolicyImplicitLog(str, Enum):
    """
    FW policy implicit log
    """

    DISABLE = DISABLE
    ENABLE = ENABLE


class Fwpolicy6ImplicitLog(str, Enum):
    """
    FW policy 6 implicit log
    """

    DISABLE = DISABLE
    ENABLE = ENABLE


class InspectionMode(str, Enum):
    """
    Inspection mode
    """

    PROXY = "proxy"
    FLOW = "flow"


class NgfwMode(str, Enum):
    """
    NGFW mode
    """

    PROFILE_BASED = "profile-based"
    POLICY_BASED = "policy-based"


class PolicyOffloadLevel(str, Enum):
    """
    Policy offload level
    """

    DISABLE = DISABLE
    DEFAULT = "default"
    DOS_OFFLOAD = "dos-offload"
    FULL_OFFLOAD = "full-offload"


class ObjectItem(BaseModel):
    """
    Policy scope item
    """

    name: str | None = None
    vdom: str | None = None


class ObjectItemList(BaseModel):
    """
    Scope list items
    """

    __root__: list[ObjectItem]


class Object(BaseModel):
    """
    Main response object
    """

    name: str | None = None
    vdom: str | None = None
    code: int | None = None
    message: str | None = None


class Settings(BaseModel, allow_population_by_field_name=True):
    """
    Policy package settings
    """

    central_nat: CentralNat | None = Field(
        default=None,
        alias="central-nat",
        description="disable -> (value 0)  enable -> (value 1)",
    )
    consolidated_firewall_mode: ConsolidatedFirewallMode | None = Field(
        default=None,
        alias="consolidated-firewall-mode",
        description="For flow-based policy package. Disable = (value 0)  enable = (value 1)",
    )
    fwpolicy_implicit_log: FwpolicyImplicitLog | None = Field(
        default=None,
        alias="fwpolicy-implicit-log",
        description="disable = (value 0), enable = (value 1)",
    )
    fwpolicy6_implicit_log: Fwpolicy6ImplicitLog | None = Field(
        default=None,
        alias="fwpolicy6-implicit-log",
        description="disable -> (value 0), enable -> (value 1)",
    )
    inspection_mode: InspectionMode | None = Field(
        default=None,
        alias="inspection-mode",
        description="proxy - (value 0) flow - (value 1) ",
    )
    ngfw_mode: NgfwMode | None = Field(
        default=None,
        alias="ngfw-mode",
        description="For flow-based policy package.profile-based - (value 0) policy-based - (value 1) ",
    )
    policy_offload_level: PolicyOffloadLevel | None = Field(
        default=None,
        alias="policy-offload-level",
        description="disable - (value 0) default - (value 1) dos-offload - (value 2) full-offload - (value 3) ",
    )
    ssl_ssh_profile: str | list[str] | None = Field(
        default=None,
        alias="ssl-ssh-profile",
        description="SSL-SSH profile required for NGFW-mode policy package.",
    )


class PolicyPackage(BaseModel, allow_population_by_field_name=True):
    """
    Policy package
    """

    name: str | None = Field(
        default=None, description="Does not include any parent folders."
    )
    obj_ver: int | None = Field(
        default=None, alias="obj ver", description="Package version."
    )
    oid: int | None = Field(default=None, description="Internal package ID.")
    package_settings: Settings | None = Field(default=None, alias="package settings")
    scope_member: Object | list[Object] | None = Field(
        default=None, alias="scope member"
    )
    subobj: list[PolicyPackage] | None = Field(
        default=None,
        description="Available if object type is 'folder', includes all policy packages and sub-folders under the folder object.",
    )
    type: Type | None = None


class FolderWithPolicyPkgs(PolicyPackage):
    """
    Folder with Policy Packages
    """
