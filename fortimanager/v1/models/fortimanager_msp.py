"""
FortiManager MSP V1 Pydantic models
"""

from pydantic import BaseModel, Field


class FortiManagerMSPV1(BaseModel):
    """
    FortiManager MSP V1 model
    """

    admin_domain_configuration: str = Field(alias="Admin Domain Configuration")
    bios_version: str = Field(alias="BIOS version")
    branch_point: str = Field(alias="Branch Point")
    build: str = Field(alias="Build")
    current_time: str = Field(alias="Current Time")
    daylight_time_saving: str = Field(alias="Daylight Time Saving")
    fips_mode: str = Field(alias="FIPS Mode")
    ha_mode: str = Field(alias="HA Mode")
    hostname: str = Field(alias="Hostname")
    license_status: str = Field(alias="License Status")
    major: str = Field(alias="Major")
    max_num_of_admin_domains: str = Field(alias="Max Number of Admin Domains")
    max_num_of_device_groups: str = Field(alias="Max Number of Device Groups")
    minor: str = Field(alias="Minor")
    offline_mode: str = Field(alias="Offline Mode")
    patch: str = Field(alias="Patch")
    platform_full_name: str = Field(alias="Platform Full Name")
    platform_type: str = Field(alias="Platform Type")
    release_ver_info: str = Field(alias="Release Version Information")
    serial: str = Field(alias="Serial Number")
    tz: str = Field(alias="TZ")
    time_zone: str = Field(alias="Time Zone")
    version: str = Field(alias="Version")
    x8664_apps: str = Field(alias="x86-64 Applications")
