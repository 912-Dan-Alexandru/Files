"""
policy package model init
"""

from .fortimanager_policy_package import (
    CentralNat,
    ConsolidatedFirewallMode,
    FolderWithPolicyPkgs,
    Fwpolicy6ImplicitLog,
    FwpolicyImplicitLog,
    NgfwMode,
    PolicyOffloadLevel,
    PolicyPackage,
    Settings,
    Type,
)

__all__ = [
    "PolicyPackage",
    "FolderWithPolicyPkgs",
    "NgfwMode",
    "PolicyOffloadLevel",
    "Type",
    "CentralNat",
    "ConsolidatedFirewallMode",
    "Fwpolicy6ImplicitLog",
    "FwpolicyImplicitLog",
    "Settings",
]
