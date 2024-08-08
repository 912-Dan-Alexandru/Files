"""
Exports
"""

from .fortimanager import SBFortiManagerV1
from .fortimanager_adoms_service import (
    add_adom_folder_or_policy_package,
    get_adom_device_groups,
    get_adom_devices,
    get_adom_folder_or_policy_package,
    get_adom_folders_and_policy_packages,
    get_adoms,
    get_device,
    modify_adom_devices,
    update_adom_folder_or_policy_package,
)

__all__ = [
    "SBFortiManagerV1",
    "get_adoms",
    "get_adom_devices",
    "get_adom_device_groups",
    "get_adom_folders_and_policy_packages",
    "get_adom_folder_or_policy_package",
    "add_adom_folder_or_policy_package",
    "get_device",
    "modify_adom_devices",
    "update_adom_folder_or_policy_package",
]
