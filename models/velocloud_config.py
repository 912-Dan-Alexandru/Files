"""
Models to configure Velocloud
"""

from pydantic import BaseModel, Field

from common.models.velocloud.velocloud_version import VelocloudVersion


class VelocloudConfig(BaseModel):
    """
    Model used to configure velocloud
    """

    version: VelocloudVersion = Field(
        description="""
            Version velocloud to use.
            """,
        default=VelocloudVersion.UNKNOWN,
    )

    url: str | None = Field(
        description="""
        Velocloud url.
        """,
        default=None,
    )
