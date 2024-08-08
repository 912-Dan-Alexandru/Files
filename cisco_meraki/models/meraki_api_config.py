"""
Model to setup the configuration for meraki api clients
"""

from pydantic import BaseModel


class MerakiApiConfig(BaseModel):
    """
    Model to setup the configuration for meraki api clients
    """

    host: str | None
    api_key: str
