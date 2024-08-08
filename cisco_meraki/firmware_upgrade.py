"""
Meraki API
/Firmware Upgrade Endpoint Functions
"""

from common.parsing import evaluate_model
from . import models
from .cisco_meraki import SBMeraki


@SBMeraki.exception_handler
def get_network_firmware_upgrade(
    client: SBMeraki, network_id: str
) -> models.FirmwareUpgradeGET:
    """
    API:  /networks/{networkId}/firmwareUpgrades
    Success 200 Response
    """
    data = client.api.networks.getNetworkFirmwareUpgrades(network_id)
    return evaluate_model(models.FirmwareUpgradeGET, data)


@SBMeraki.exception_handler
def update_network_firmware_upgrade(
    client: SBMeraki,
    network_id: str,
    firmware_upgrade_data: models.FirmwareUpgradePUT,
) -> models.FirmwareUpgradeGET:
    """
    API:  /networks/{networkId}/firmwareUpgrades
    Success 200 Response
    """
    data = client.api.networks.updateNetworkFirmwareUpgrades(
        network_id, **firmware_upgrade_data.dict(exclude_none=True)
    )
    return evaluate_model(models.FirmwareUpgradeGET, data)
