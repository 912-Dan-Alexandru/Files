"""
Fortinet utils
"""

from pydantic import parse_obj_as

from common.southbound.fortimanager.v1 import SBFortiManagerV1
from common.tools.tmf_logger import TMFLogger

from .messages import SBFortiManagerV1Messages as Messages
from .models.fortimanager_api_config import FortinetApiConfig

logger = TMFLogger()


def get_fortinet_api_config(fortinet_config_list: list[dict]):
    """
    Fortinet config fit to model
    """
    try:
        return parse_obj_as(list[FortinetApiConfig], fortinet_config_list)
    except ValueError:
        logger.log(Messages.ERROR_PARSING_FORTINET_CONFIG)
        return None


def get_fortinet_api_client(fortinet_api_config_list: list[FortinetApiConfig] | None):
    """
    Creates a list of SBFortiManagerV1 instances from the provided API configuration
    """
    if not fortinet_api_config_list:
        logger.log(Messages.ERROR_CREATING_FORTINET_CLIENT)
        return None
    return [
        SBFortiManagerV1(**forti_api_config.dict())
        for forti_api_config in fortinet_api_config_list
    ]
