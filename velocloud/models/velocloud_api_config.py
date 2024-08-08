"""
Model to setup the configuration for velocloud api clients
"""

from pydantic import BaseModel

from common.models.velocloud.velocloud_version import VelocloudVersion


class VelocloudApiConfig(BaseModel):
    """
    Model to setup the configuration for velocloud api clients
    """

    host: str
    api_key: str
    version: VelocloudVersion
