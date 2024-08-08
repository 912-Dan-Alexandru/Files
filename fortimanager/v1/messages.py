"""
SBFortiManagerV1 log Messages
"""

from common.tools.tmf_logger import LogLevel, TMFMessage


class SBFortiManagerV1Messages(TMFMessage):
    """
    Log Messages for SBFortiManagerV1 class
    """

    LOGIN_ERROR = (LogLevel.ERROR, "Fortinet API - Login fail.")
    API_REQUEST_FAILED = (LogLevel.ERROR, "FortiManager API Request Failed")
    ERROR_PARSING_FORTINET_CONFIG = (
        LogLevel.ERROR,
        "Unable to parse fortinet config to model",
    )
    ERROR_CREATING_FORTINET_CLIENT = (
        LogLevel.ERROR,
        "Unable to create fortinet client",
    )
