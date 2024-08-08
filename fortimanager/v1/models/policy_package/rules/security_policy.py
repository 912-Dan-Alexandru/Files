"""
Fortimanager security policy rule model
"""

# pylint: disable=line-too-long
from enum import Enum

from pydantic import BaseModel, Field

from common.southbound.fortimanager.v1.models.policy_package.rules.common.enums import (
    LogtrafficEnum,
    ProfileTypeEnum,
    StatusEnum,
)
from common.southbound.fortimanager.v1.models.policy_package.rules.firewall_policy import (
    PolicyRule,
)


class ActionEnum(Enum):
    """
    Rule action
    """

    ACCEPT = "accept"  # 1
    DENY = "deny"  # 0


class FirewallSecurityPolicyCommonProps(BaseModel):
    """
    Configure NGFW IPv4/IPv6 application policies.
    """

    _policy_block: int = Field(...)
    action: ActionEnum = Field(
        default=ActionEnum.DENY, description="Policy action (accept/deny)."
    )

    application_list: list[str] = Field(
        ...,
        alias="application-list",
        description="Name of an existing Application list.",
    )
    av_profile: list[str] = Field(
        ..., alias="av-profile", description="Name of an existing Antivirus profile."
    )
    casb_profile: list[str] = Field(
        ..., alias="casb-profile", description="Name of an existing CASB profile."
    )
    comments: str = Field(..., description="Comment.", max_length=1023)
    diameter_filter_profile: list[str] = Field(
        ...,
        alias="diameter-filter-profile",
        description="Name of an existing Diameter filter profile.",
    )
    dlp_profile: list[str] = Field(
        ..., alias="dlp-profile", description="Name of an existing DLP profile."
    )
    dnsfilter_profile: list[str] = Field(
        ...,
        alias="dnsfilter-profile",
        description="Name of an existing DNS filter profile.",
    )
    dstaddr: list[str] = Field(
        ..., description="Destination IPv4 address name and address group names."
    )
    dstaddr_negate: StatusEnum = Field(
        alias="dstaddr-negate",
        default=StatusEnum.DISABLE,
        description="When enabled dstaddr specifies what the destination address"
        " must NOT be.",
    )
    dstaddr6: list[str] = Field(
        ..., description="Destination IPv6 address name and address group names."
    )
    dstaddr6_negate: StatusEnum = Field(
        alias="dstaddr6-negate",
        default=StatusEnum.DISABLE,
        description="When enabled dstaddr6 specifies what the destination address"
        " must NOT be.",
    )
    dstintf: list[str] = Field(..., description="Outgoing (egress) interface.")

    file_filter_profile: list[str] = Field(
        ...,
        alias="file-filter-profile",
        description="Name of an existing file-filter profile.",
    )
    fsso_groups: list[str] = Field(
        ..., alias="fsso-groups", description="Names of FSSO groups."
    )
    global_label: str = Field(
        ...,
        alias="global-label",
        description="Label for the policy that appears when the GUI is in Global"
        " View mode.",
        max_length=63,
    )
    groups: list[str] = Field(
        ..., description="Names of user groups that can authenticate with this policy."
    )
    icap_profile: list[str] = Field(
        ..., alias="icap-profile", description="Name of an existing ICAP profile."
    )
    internet_service: StatusEnum = Field(
        alias="internet-service",
        default=StatusEnum.DISABLE,
        description="Enable/disable use of Internet Services for this policy."
        " If enabled, destination address, service and default application"
        " port enforcement are not used.",
    )
    internet_service_custom: list[str] = Field(
        ...,
        alias="internet-service-custom",
        description="Custom Internet Service name.",
    )
    internet_service_custom_group: list[str] = Field(
        ...,
        alias="internet-service-custom-group",
        description="Custom Internet Service group name.",
    )
    internet_service_group: list[str] = Field(
        ..., alias="internet-service-group", description="Internet Service group name."
    )
    internet_service_name: list[str] = Field(
        ..., alias="internet-service-name", description="Internet Service name."
    )
    internet_service_negate: StatusEnum = Field(
        alias="internet-service-negate",
        default=StatusEnum.DISABLE,
        description="When enabled internet-service specifies what the service"
        " must NOT be.",
    )
    internet_service_src: StatusEnum = Field(
        alias="internet-service-src",
        default=StatusEnum.DISABLE,
        description="Enable/disable use of Internet Services in source for"
        " this policy. If enabled, source address is not used.",
    )
    internet_service_src_custom: list[str] = Field(
        ...,
        alias="internet-service-src-custom",
        description="Custom Internet Service source name.",
    )
    internet_service_src_custom_group: list[str] = Field(
        ...,
        alias="internet-service-src-custom-group",
        description="Custom Internet Service source group name.",
    )
    internet_service_src_group: list[str] = Field(
        ...,
        alias="internet-service-src-group",
        description="Internet Service source group name.",
    )
    internet_service_src_name: list[str] = Field(
        ...,
        alias="internet-service-src-name",
        description="Internet Service source name.",
    )
    internet_service_src_negate: StatusEnum = Field(
        alias="internet-service-src-negate",
        default=StatusEnum.DISABLE,
        description="When enabled internet-service-src specifies what"
        " the service must NOT be.",
    )
    internet_service6: StatusEnum = Field(
        alias="internet-service6",
        default=StatusEnum.DISABLE,
        description="Enable/disable use of IPv6 Internet Services for "
        "this policy. If enabled, destination address, service and default"
        " application port enforcement are not used.",
    )
    internet_service6_custom: list[str] = Field(
        ...,
        alias="internet-service6-custom",
        description="Custom IPv6 Internet Service name.",
    )
    internet_service6_custom_group: list[str] = Field(
        ...,
        alias="internet-service6-custom-group",
        description="Custom IPv6 Internet Service group name.",
    )
    internet_service6_group: list[str] = Field(
        ..., alias="internet-service6-group", description="Internet Service group name."
    )
    internet_service6_name: list[str] = Field(
        ..., alias="internet-service6-name", description="IPv6 Internet Service name."
    )
    internet_service6_negate: StatusEnum = Field(
        alias="internet-service6-negate",
        default=StatusEnum.DISABLE,
        description="When enabled internet-service6 specifies what the "
        "service must NOT be.",
    )
    internet_service6_src: StatusEnum = Field(
        alias="internet-service6-src",
        default=StatusEnum.DISABLE,
        description="Enable/disable use of IPv6 Internet Services in source"
        " for this policy. If enabled, source address is not used.",
    )
    internet_service6_src_custom: list[str] = Field(
        ...,
        alias="internet-service6-src-custom",
        description="Custom IPv6 Internet Service source name.",
    )
    internet_service6_src_custom_group: list[str] = Field(
        ...,
        alias="internet-service6-src-custom-group",
        description="Custom Internet Service6 source group name.",
    )
    internet_service6_src_group: list[str] = Field(
        ...,
        alias="internet-service6-src-group",
        description="Internet Service6 source group name.",
    )
    internet_service6_src_name: list[str] = Field(
        ...,
        alias="internet-service6-src-name",
        description="IPv6 Internet Service source name.",
    )
    internet_service6_src_negate: StatusEnum = Field(
        alias="internet-service6-src-negate",
        default=StatusEnum.DISABLE,
        description="When enabled internet-service6-src specifies what "
        "the service must NOT be.",
    )
    ips_sensor: list[str] = Field(
        ..., alias="ips-sensor", description="Name of an existing IPS sensor."
    )
    ips_voip_filter: list[str] = Field(
        ...,
        alias="ips-voip-filter",
        description="Name of an existing VoIP (ips) profile.",
    )

    logtraffic: LogtrafficEnum = Field(
        default=LogtrafficEnum.UTM,
        description="Enable or disable logging. Log all sessions or security"
        " profile sessions.",
    )
    name: str = Field(..., description="Policy name.", max_length=35)
    nat46: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable NAT46."
    )
    nat64: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable NAT64."
    )
    policyid: int = Field(default=0, description="Policy ID.", le=4294967294)
    profile_group: list[str] = Field(
        ..., alias="profile-group", description="Name of profile group."
    )
    profile_protocol_options: list[str] = Field(
        alias="profile-protocol-options",
        default="default",
        description="Name of an existing Protocol options profile.",
    )
    profile_type: ProfileTypeEnum = Field(
        alias="profile-type",
        default=ProfileTypeEnum.SINGLE,
        description="Determine whether the firewall policy allows security"
        " profile groups or single profiles only.",
    )
    schedule: list[str] = Field(..., description="Schedule name.")
    sctp_filter_profile: list[str] = Field(
        ...,
        alias="sctp-filter-profile",
        description="Name of an existing SCTP filter profile.",
    )
    send_deny_packet: StatusEnum = Field(
        alias="send-deny-packet",
        default=StatusEnum.DISABLE,
        description="Enable to send a reply when a session is denied "
        "or blocked by a firewall policy.",
    )
    service: list[str] = Field(..., description="Service and service group names.")
    service_negate: StatusEnum = Field(
        alias="service-negate",
        default=StatusEnum.DISABLE,
        description="When enabled service specifies what the service must NOT be.",
    )
    srcaddr: list[str] = Field(
        ..., description="Source IPv4 address name and address group names."
    )
    srcaddr_negate: StatusEnum = Field(
        alias="srcaddr-negate",
        default=StatusEnum.DISABLE,
        description="When enabled srcaddr specifies what the source "
        "address must NOT be.",
    )
    srcaddr6: list[str] = Field(
        ..., description="Source IPv6 address name and address group names."
    )
    srcaddr6_negate: StatusEnum = Field(
        alias="srcaddr6-negate",
        default=StatusEnum.DISABLE,
        description="When enabled srcaddr6 specifies what the source "
        "address must NOT be.",
    )
    srcintf: list[str] = Field(..., description="Incoming (ingress) interface.")
    ssh_filter_profile: list[str] = Field(
        ...,
        alias="ssh-filter-profile",
        description="Name of an existing SSH filter profile.",
    )
    status: StatusEnum = Field(
        default=StatusEnum.ENABLE, description="Enable or disable this policy."
    )

    users: list[str] = Field(
        ...,
        description="Names of individual users that can authenticate with this policy.",
    )
    utm_status: StatusEnum = Field(
        alias="utm-status",
        default=StatusEnum.ENABLE,
        description="Enable security profiles.",
    )
    uuid: str = Field(
        default="00000000-0000-0000-0000-000000000000",
        description="Universally Unique Identifier "
        "(UUID; automatically assigned but can be manually reset).",
    )
    videofilter_profile: list[str] = Field(
        ...,
        alias="videofilter-profile",
        description="Name of an existing VideoFilter profile.",
    )
    virtual_patch_profile: list[str] = Field(
        ...,
        alias="virtual-patch-profile",
        description="Name of an existing virtual-patch profile.",
    )
    voip_profile: list[str] = Field(
        ...,
        alias="voip-profile",
        description="Name of an existing VoIP (voipd) profile.",
    )
    webfilter_profile: list[str] = Field(
        ...,
        alias="webfilter-profile",
        description="Name of an existing Web filter profile.",
    )


class FirewallSecurityPolicy(FirewallSecurityPolicyCommonProps):
    """
    Security groups
    """

    app_category: list[str] = Field(
        ..., alias="app-category", description="Application category ID list."
    )
    app_group: list[str] = Field(
        ..., alias="app-group", description="Application group names."
    )
    application: list[int] = Field(..., description="Application ID list.")

    enforce_default_app_port: StatusEnum = Field(
        alias="enforce-default-app-port",
        default=StatusEnum.ENABLE,
        description="Enable/disable default application port enforcement for "
        "allowed applications.",
    )

    emailfilter_profile: list[str] = Field(
        ...,
        alias="emailfilter-profile",
        description="Name of an existing email filter profile.",
    )

    learning_mode: StatusEnum = Field(
        alias="learning-mode",
        default=StatusEnum.DISABLE,
        description="Enable to allow everything, but log all of the meaningful "
        "data for security information gathering. A learning report will be generated.",
    )
    url_category: list[str] = Field(
        ..., alias="url-category", description="URL categories or groups."
    )


class FortiManagerSecurityPolicyV1(PolicyRule):
    """
    Configure NGFW IPv4/IPv6 application policies.
    """

    action: ActionEnum = Field(
        default=ActionEnum.DENY, description="Policy action (accept/deny)."
    )
    url_category: list[str] = Field(
        default=[], alias="url-category", description="URL categories or groups."
    )
    application: list[int] = Field(default=[], description="Application ID list.")
