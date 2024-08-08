"""
export all fortimanager models
"""

from .central_dnat import FortiManagerCentralDnatV1
from .central_ipv6_dnat import FortiManagerCentralDnat6V1
from .central_snat import FortiManagerCentralSnatV1
from .firewall_policy import FortiManagerFirewallPolicyV1
from .policy_header_footer import FortiManagerHeaderFooterPolicyV1
from .security_policy import FortiManagerSecurityPolicyV1
from .virtual_ip import FortiManagerFirewallVipV1
from .virtual_ip_6 import FortiManagerFirewallVip6V1

__all__ = [
    "FortiManagerCentralDnat6V1",
    "FortiManagerCentralDnatV1",
    "FortiManagerCentralSnatV1",
    "FortiManagerFirewallPolicyV1",
    "FortiManagerHeaderFooterPolicyV1",
    "FortiManagerSecurityPolicyV1",
    "FortiManagerFirewallVipV1",
    "FortiManagerFirewallVip6V1",
]
