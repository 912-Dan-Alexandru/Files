"""
Log Messages used in /common/southbound/ist
"""

from common.tools.tmf_logger import LogLevel, TMFMessage


class MistMessages(TMFMessage):
    """
    Log Messages for mist class
    """

    ERROR_PARSING_MIST_CONFIG = (LogLevel.ERROR, "Unable to parse mist config to model")
    ERROR_CREATING_MIST_CLIENT = (
        LogLevel.ERROR,
        "Unable to create mist client",
    )
