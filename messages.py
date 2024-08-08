"""
Message Class
"""

from common.tools.tmf_logger import LogLevel, TMFMessage


class VelocloudApiCallMessages(TMFMessage):
    """
    Velocloud API call Messages
    """

    EVENT_FAILING_PARSING = (LogLevel.INFO, "Number of failed event parsed")
    RUNTIME_API_ERROR = (LogLevel.ERROR, "API Call Failed")
    ERROR_PARSING_VELOCLOUD_CONFIG = (
        LogLevel.ERROR,
        "Unable to parse velocloud config to model",
    )
    ERROR_CREATING_VELOCLOUD_CLIENT = (
        LogLevel.ERROR,
        "Unable to create velocloud client",
    )
