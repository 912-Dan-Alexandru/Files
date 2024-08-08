"""
Velocloud utils
"""

from pydantic import parse_obj_as

from common.southbound.velocloud.velocloud import SBVelocloud
from common.tools.tmf_logger import TMFLogger

from .messages import VelocloudApiCallMessages as Messages
from .models.velocloud_api_config import VelocloudApiConfig

logger = TMFLogger()


def get_velocloud_api_config(velocloud_config_list: list[dict]):
    """
    Velocloud config fit to model
    """
    try:
        return parse_obj_as(list[VelocloudApiConfig], velocloud_config_list)
    except ValueError:
        logger.log(Messages.ERROR_PARSING_VELOCLOUD_CONFIG)
        return None


def get_velocloud_api_client(
    velocloud_api_config_list: list[VelocloudApiConfig] | None,
):
    """
    Creates a list of SBVelocloud instances from the provided API configuration
    """
    if not velocloud_api_config_list:
        logger.log(Messages.ERROR_CREATING_VELOCLOUD_CLIENT)
        return None
    return [
        SBVelocloud(**velocloud_api_config.dict())
        for velocloud_api_config in velocloud_api_config_list
    ]
