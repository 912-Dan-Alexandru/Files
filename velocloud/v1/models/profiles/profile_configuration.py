"""
Velocloud V1 Profile/configuration
"""
from __future__ import annotations
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field

from common.southbound.velocloud.v1.models.profiles.profile_module import (
    ConfigurationModule,
)


class ConfigurationType(Enum):
    """
    Profile configuration type
    """

    NETWORK_BASED = "NETWORK_BASED"
    SEGMENT_BASED = "SEGMENT_BASED"


class ConfigurationCloneEnterpriseTemplate(BaseModel):
    """
    Model used for creation of a configuration/profile
    """

    enterpriseId: int = Field(
        description="Required if called from the operator or MSP context"
        " identifies the target enterprise of the API call."
    )
    name: str = Field(description="Profile/configuration name")
    description: str = Field(description="Short description of the profile")
    configurationType: ConfigurationType | None = Field(
        None,
        description="If both"
        "network and segment based functionality is granted to the enterprise,"
        " chose which template type to clone. If not specified the type of the"
        " operator profile assigned to the enterprise will be used",
    )


class ConfigurationCloneEnterpriseTemplateResult(BaseModel):
    """
    The result of the profile creation operation, containing the
    ID of the newly cloned configuration."""

    id: int


class ConfigurationDeleteConfiguration(BaseModel):
    """
    Model used as input for the profile cancellation API
    """

    enterprise_id: int | None = Field(alias="enterpriseId")
    id: int = Field(..., description="Configuration ID")


class EntityStateChangeOutcomeConfirmation(BaseModel):
    """
    Model that reflects  the output of the profile cancellation or update operation
    """

    id: int | None = Field(None, description="The id of the deleted object.")
    error: str | None = Field(
        None, description="An error message explaining why the method failed"
    )
    rows: int | None = Field(None, description="The number of rows modified")


class BastionState(Enum):
    """
    Bastion state enum
    """

    UNCONFIGURED = "UNCONFIGURED"
    STAGE_REQUESTED = "STAGE_REQUESTED"
    UNSTAGE_REQUESTED = "UNSTAGE_REQUESTED"
    STAGED = "STAGED"
    UNSTAGED = "UNSTAGED"


class Tinyint(Enum):
    """
    Enable/Disable enum
    """

    INTEGER_0 = 0
    INTEGER_1 = 1


class VelocloudProfileConfiguration(BaseModel):
    """
    Velocloud Profile/Configuration main model
    """

    bastion_state: BastionState | None = Field(None, alias="bastionState")
    configuration_type: ConfigurationType | None = Field(
        None, alias="configurationType"
    )
    created: datetime | None = None
    description: str | None = None
    edge_count: int | None = Field(None, alias="edgeCount")
    effective: datetime | None = None
    enterprise_logical_id: str | None = Field(None, alias="enterpriseLogicalId")
    id: int | None = None
    is_staging: Tinyint | None = Field(None, alias="isStaging")
    logical_id: str | None = Field(None, alias="logicalId")
    modified: datetime | None = None
    modules: list[ConfigurationModule] | None = None
    name: str | None = None
    schema_version: str | None = Field(None, alias="schemaVersion")
    version: str | None = None


class VelocloudProfileConfigurationUpdate(BaseModel):
    """
    Model used for Configuration/Profile general/minor updates
    """

    id: int
    name: str | None = None
    description: str | None = None
    version: str | None = None
    effective: str | None = None
