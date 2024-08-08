"""
CLI Template FortiManager model
"""

from enum import Enum

from pydantic import BaseModel, Field


class PositionEnum(Enum):
    """
    Defines the position where the template should be applied in the process.
    """

    POST_VDOM_COPY = "post-vdom-copy"
    PREP_VDOM_COPY = "prep-vdom-copy"


class ProvisionEnum(Enum):
    """
    Indicates whether the template is a Pre-Run CLI Template or a simple CLI Template.
    """

    DISABLE = "disable"
    ENABLE = "enable"


class CLITypeEnum(Enum):
    """
    Specifies the type of template.
    """

    CLI = "cli"
    JINJA = "jinja"


class FortiManagerCliTemplateV1(BaseModel):
    """
    FortiManager CLI template v1 model
    """

    name: str = Field(
        ...,
        description=(
            "The name of the template. This field is required and should be unique "
            "to identify the template."
        ),
    )
    description: str = Field(
        ...,
        max_length=4096,
        description=(
            "A detailed description of the template. This field can hold up to "
            "4096 characters."
        ),
    )
    position: PositionEnum = Field(
        ...,
        description=(
            "Defines when the template should be applied in relation to the VDOM "
            "copy process."
        ),
    )
    provision: ProvisionEnum = Field(
        ...,
        description=(
            "Indicates if the template is a simple CLI Template or a Pre-Run CLI "
            "Template. A Pre-Run CLI Template runs once when onboarding a new device, "
            "executed before the system provisioning templates. Only applicable on "
            "model devices."
        ),
    )
    script: str = Field(
        ...,
        description=(
            "The actual CLI commands or Jinja script that the template will execute. "
            "This field contains the core configuration logic."
        ),
    )
    type: CLITypeEnum = Field(
        ...,
        description=(
            "Specifies whether the template is a CLI template or a Jinja template."
        ),
    )
    variables: list[str] = Field(
        ...,
        description=(
            "A list of variables used in the template. This allows for dynamic "
            "content generation within the script."
        ),
    )
