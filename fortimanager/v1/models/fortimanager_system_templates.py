"""
FortiManager System Templates V1 Pydantic models
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

from common.southbound.fortimanager.v1.models.fortimanager_dns import (
    FortiManagerModifyDeviceSystemDnsV1,
)


class SystemTemplateOptions(str, Enum):
    """
    Options that can be enabled for a determined System template
    """

    ADMIN = "admin"
    COMBINED = "combined"
    DNS = "dns"
    EMAIL = "email"
    FTGD = "ftgd"
    INTERFACE = "interface"
    LOG = "log"
    NTP = "ntp"
    REPMSG = "repmsg"
    ROUTER = "router"
    SNMP = "snmp"


class ScopeMember(BaseModel):
    """
    Model that defines the member to which the template applies
    """

    name: str
    vdom: str


class CreateSystemTemplate(BaseModel):
    """
    Fortinet System template model used for creation operation of
    a System template
    """

    name: str
    type: str = "devprof"
    description: str


class UpdateSystemTemplate(BaseModel):
    """
    Fortinet System template model used for update operation of
    a System template
    """

    description: str | None = None


class FortinetSystemTemplate(CreateSystemTemplate, UpdateSystemTemplate):
    """
    Fortinet System template main model
    """

    enabled_options: list[SystemTemplateOptions] = Field(..., alias="enabled options")
    oid: int
    scope_member: list[ScopeMember] | None = Field(None, alias="scope member")


class UpdateSystemTemplateEnabledSettings(
    BaseModel, allow_population_by_field_name=True
):
    """
    System template available setting options model used
    for enabling/disabling settings options for a
    FortinetSystemTemplate
    """

    description: str | None = None
    enabled_pages: list[SystemTemplateOptions] = Field(alias="enabled-pages")


class SystemTemplateEnabledSettings(UpdateSystemTemplateEnabledSettings):
    """
    System template available setting options model
    """

    flags: int
    oid: int


class SystemTemplateDNSVariableNames(str, Enum):
    """
    Variable names
    """

    TIMEOUT = "system dns/timeout"
    CERTIFICATE = "system dns/ssl-certificate"
    SERVER_HOSTNAME = "system dns/server-hostname"
    RETRY = "system dns/retry"
    DNS_OVER_TLS = "system dns/dns-over-tls"
    CACHE_TTL = "system dns/dns-cache-ttl"
    CACHE_LIMIT = "system dns/dns-cache-limit"
    CACHE_NOT_FOUND = "system dns/cache-notfound-responses"
    DOMAIN = "system dns/domain"
    SECONDARY = "system dns/secondary"
    PRIMARY = "system dns/primary"


class SystemTemplateDNSVariables(BaseModel):
    """
    System template DNS variables
    """

    name: str
    oid: int
    override: int | None


class UpdateSystemTemplateDNSWidget(BaseModel):
    """
    Fortinet System template model used for update operation of
    a System template DNS setting configuration
    """

    model: str = "all"
    value: FortiManagerModifyDeviceSystemDnsV1 | None = None


class CreateSystemTemplateDNSWidget(UpdateSystemTemplateDNSWidget):
    """
    Fortinet System template model used for creation operation of
    a System template DNS setting configuration
    """

    action: str = "conf-sys-dns"
    seq: int


class SystemTemplateDNSWidget(CreateSystemTemplateDNSWidget):
    """
    DNS configuration option for System template
    """

    dynamic_mapping: Any = None
    oid: int
    var_list: list[SystemTemplateDNSVariables] | None = Field(
        alias="var-list", default=None
    )


class SystemTemplateEmailWidget(BaseModel):
    """
    Email configuration option for System template
    """

    action: str = "conf-sys-email"
    seq: int
    dynamic_mapping: Any
    oid: int


class SystemTemplateLogWidget(BaseModel):
    """
    Log configuration option for System template
    """

    action: str = "conf-sys-log"
    seq: int
    dynamic_mapping: Any
    oid: int
