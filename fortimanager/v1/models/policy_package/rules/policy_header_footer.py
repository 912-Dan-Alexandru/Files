"""
Fortimanager Footer/Header rules model
"""

# pylint: disable=line-too-long
from pydantic import Field

from common.southbound.fortimanager.v1.models.policy_package.rules.firewall_policy import (
    FirewallPolicyCommonProps,
    FortiManagerFirewallPolicyV1,
)


class GlobalHeaderFooterPolicy(FirewallPolicyCommonProps):
    """
    Configure Global Header/Footer Policy
    """

    gtp_profile: list[str] = Field(..., alias="gtp-profile")
    pfcp_profile: list[str] = Field(..., alias="pfcp-profile")


class FortiManagerHeaderFooterPolicyV1(FortiManagerFirewallPolicyV1):
    """
    Fortimanager header footer policy v1
    """
