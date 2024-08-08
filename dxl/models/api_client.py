"""
APIClient models
"""
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from common.models.message_bus import SecurityProtocolConfig


class TokenResponse(BaseModel):
    """
    Model for the token response
    """

    access_token: str
    token_type: str
    expires_in: str
    issued_at: str
    scope: str


class RequestHeaders(BaseModel):
    """
    RequestHeaders model class
    """

    x_route_info: Optional[str] = Field(alias="x-route-info", default=None)
    x_country_code: Optional[str] = Field(alias="x-country-code", default=None)
    x_source_system: Optional[str] = Field(alias="x-source-system", default=None)
    x_destination_system: Optional[str] = Field(
        alias="x-destination-system", default=None
    )
    x_transaction_id: str = Field(..., alias="x-transaction-id")
    authorization: str = Field(..., alias="Authorization")


class AuthBody(BaseModel):
    """
    AuthBody model
    """

    client_id: str
    client_secret: str
    grant_type: str
    scope: str


class MutualSSLConfig(BaseModel):
    """
    Mutual SSL Configuration Items
    """

    cert_public: str = Field(description="Public Certificate to be sent")
    cert_private: str = Field(description="Private Key to decrypt data")
    cert_passphrase: Optional[str] = Field(
        default=None, description="Passphrase to decrypt private key"
    )


class AuthTypes(str, Enum):
    """
    Auth Types
    """

    NONE = "none"
    OAUTH = "oauth"
    BASIC = "basic"


class AuthOAuthConfig(BaseModel):
    """
    OAuth Specific Auth Variables
    """

    client_id: str = Field(description="OAuth Key")
    client_secret: str = Field(description="OAuth secret")
    scope: str = Field(description="OAuth Scopes")
    token_endpoint: str = Field(description="OAuth Token Endpoint")


class AuthBasic(BaseModel):
    """
    Basic Auth Configuration
    Username and Password Auth
    """

    username: str = Field(description="Basic Auth Username")
    password: str = Field(description="Basic Auth Password", repr=False)


class DXLConfig(BaseModel, allow_population_by_field_name=True):
    """
    DXL Specific Configuration
    e.g. API Routing Header Values
    """

    x_country_code: Optional[str] = Field(
        default=None,
        description="""
        DXL Routes to Different Instances Based on this key
        Examples:
            - GRP
            - IT
            - DE
        """,
        alias="x-country-code",
    )
    x_route_info: Optional[str] = Field(
        default=None,
        description="""
        DXL Application Routing Key
        Examples:
            - sdwan.velocloud
        """,
        alias="x-route-info",
    )
    x_source_system: Optional[str] = Field(
        default=None,
        description="""
        Used by SNOW DXL
        Examples:
            - Cisco Meraki
        """,
        alias="x-source-system",
    )
    x_destination_system: Optional[str] = Field(
        default=None,
        description="""
        Used by SNOW DXL
        Examples:
            - SNOW
        """,
        alias="x-destination-system",
    )


class AuthConfig(BaseModel):
    """
    Oauth Configuration for Token Generation
    """

    type: AuthTypes = Field(
        description="Type of Authentication", default=AuthTypes.NONE
    )
    oauth: AuthOAuthConfig | None = Field(
        default=None, description="Oauth Configuration"
    )
    basic: AuthBasic | None = Field(
        default=None, description="Basic Auth Configuration"
    )
    dxl: DXLConfig | None = Field(
        default=None, description="DXL Specific Configuration"
    )
    mutual_ssl: MutualSSLConfig | None = Field(
        default=None, description="Mutual SSL Configuration"
    )
    kafka_security: SecurityProtocolConfig | None = Field(
        default=None, description="Security protocol configuration for kafka clients"
    )
