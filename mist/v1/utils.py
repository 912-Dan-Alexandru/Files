"""
Mist utils
"""

from pydantic import parse_obj_as

from common.southbound.mist.v1 import SBMistV1
from common.tools.tmf_logger import TMFLogger

from .messages import MistMessages as Messages
from .models.mist_api_config import MistApiConfig

logger = TMFLogger()


def get_mist_api_config(mist_config_list: list[dict]):
    """
    Mist config fit to model
    """
    try:
        return parse_obj_as(list[MistApiConfig], mist_config_list)
    except ValueError:
        logger.log(Messages.ERROR_PARSING_MIST_CONFIG)
        return None


def get_mist_api_client(mist_api_config_list: list[MistApiConfig] | None):
    """
    Creates a list of SBMistV1 instances from the provided API configuration
    """
    if not mist_api_config_list:
        logger.log(Messages.ERROR_CREATING_MIST_CLIENT)
        return None
    return [
        SBMistV1(**mist_api_config.dict()) for mist_api_config in mist_api_config_list
    ]
