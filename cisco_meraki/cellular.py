"""
Meraki API
*/cellular/* Endpoint Functions
"""
from meraki.exceptions import APIError

from common.parsing import evaluate_model
from common.tools import TMFLogger

from .messages import MerakiMessages as Messages
from .models import CellularSimcardList
from .cisco_meraki import SBMeraki


@SBMeraki.exception_handler
def get_cellular_simcards(client: SBMeraki, serial: str) -> CellularSimcardList:
    """
    API: GET /devices/{serial}/cellular/sims
    """
    try:
        data = client.api.devices.getDeviceCellularSims(serial)
    except APIError as exc:
        if (
            "This device's firmware does not support SIM configurations."
            in exc.response.json()["errors"]
        ):
            TMFLogger().log(Messages.FIRMWARE_OUT_OF_DATE, serial=serial)
            return CellularSimcardList()
        raise exc
    return evaluate_model(CellularSimcardList, data)


@SBMeraki.exception_handler
def update_cellular_simcards(
    client: SBMeraki, serial: str, update_request: CellularSimcardList
) -> CellularSimcardList:
    """
    API: PUT /devices/{serial}/cellular/sims
    """
    data = client.api.devices.updateDeviceCellularSims(
        serial, **update_request.dict(exclude_unset=True)
    )
    return evaluate_model(CellularSimcardList, data)
