"""
Model to setup the configuration for fortinet api clients
"""

from pydantic import BaseModel


class FortinetApiConfig(BaseModel):
    """
    Model to setup the configuration for fortinet
    """

    host: str
    verify_ssl: bool
    username: str
    password: str
