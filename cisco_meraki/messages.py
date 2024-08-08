"""
Log Messages used in /common/southbound/cisco_meraki
"""

from common.tools.tmf_logger import LogLevel, TMFMessage


class MerakiMessages(TMFMessage):
    "/common/southbound/cisco_meraki Log Messages"

    APIKEY_NOT_SET_ERROR = (LogLevel.ERROR, "No API key has been provided")
    MERAKI_RETURNED_ERROR = (LogLevel.ERROR, "Meraki returned an error")
    MERAKI_UNSUPPORTED_OPERATION = (
        LogLevel.WARNING,
        "Meraki endpoint is not supported for this specific context",
    )
    VALIDATION_ERROR = (LogLevel.ERROR, "Error validating API Response")
    MERAKI_CHANGE = LogLevel.INFO, "Meraki list change request detected"
    MERAKI_ADDED = LogLevel.INFO, "New Meraki added"
    MERAKI_DUPLICATE = LogLevel.WARNING, "Meraki already exists. Not adding..."
    MERAKI_NOT_FOUND = (
        LogLevel.WARNING,
        "Meraki not found. Cannot change any internal list",
    )
    MERAKI_LIST_CHANGED = LogLevel.INFO, "Meraki list changed"
    MERAKI_NETWORK_NOT_EXIST = (
        LogLevel.ERROR,
        "Unable to query networks as we don't have API access to this org",
    )
    CONFIG_TEMPLATES = (
        LogLevel.ERROR,
        "ConfigTemplates not exists",
    )
    ORGANIZATION_NOT_EXISTS = (
        LogLevel.ERROR,
        "Organization not exists",
    )
    DEVICE_NOT_EXISTS = (
        LogLevel.ERROR,
        "Device not exists",
    )
    ORGANIZATION_NOT_FOUND = (
        LogLevel.WARNING,
        "Organization not found inside the Meraki whitelist",
    )
    FIRMWARE_OUT_OF_DATE = (
        LogLevel.WARNING,
        "Cellular simcards unavailable due to unsupported firmware version",
    )
    UNSUPPORTED_REQUEST = (
        LogLevel.WARNING,
        "Unsupported for networks without a failover capable MX",
    )
    ERROR_PARSING_MERAKI_CONFIG = (
        LogLevel.ERROR,
        "Unable to parse meraki config to model",
    )
    ERROR_CREATING_MERAKI_CLIENT = (
        LogLevel.ERROR,
        "Unable to create meraki client",
    )
