"""
Meraki utils
"""

from pydantic import parse_obj_as

from common.southbound.cisco_meraki import SBMeraki
from common.tools.tmf_logger import TMFLogger

from .messages import MerakiMessages as Messages
from .models.meraki_api_config import MerakiApiConfig

logger = TMFLogger()


def get_meraki_api_config(meraki_config_list: list[dict]):
    """
    Meraki config fit to model
    """
    try:
        return parse_obj_as(list[MerakiApiConfig], meraki_config_list)
    except ValueError:
        logger.log(Messages.ERROR_PARSING_MERAKI_CONFIG)
        return None


def get_meraki_api_client(meraki_api_config_list: list[MerakiApiConfig] | None):
    """
    Creates a list of SBMeraki instances from the provided API configuration
    """
    if not meraki_api_config_list:
        logger.log(Messages.ERROR_CREATING_MERAKI_CLIENT)
        return None
    return [
        SBMeraki(**meraki_api_config.dict())
        for meraki_api_config in meraki_api_config_list
    ]
