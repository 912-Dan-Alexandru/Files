"""network configuration template models"""

from typing import List
from pydantic import BaseModel, Field

from common.southbound.cisco_meraki.models.network import ProductTypes


class ConfigurationTemplate(BaseModel):
    """
    Network Configuration Template
    https://developer.cisco.com/meraki/api-v1/get-organization-config-templates/
    """

    id: str = Field(..., description="identifier of the template")
    name: str | None = Field(default=None, description="name for the template")
    productTypes: List[ProductTypes] = Field(
        ...,
        description="product types supported in the network"
        + "(combined networks have more than one product type)",
    )
    timeZone: str | None = Field(
        default=None, description="Timezone used in the template"
    )
