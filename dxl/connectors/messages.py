"""
Message bus log Messages
"""

from common.tools.tmf_logger import LogLevel, TMFMessage


class CatalogConnectorMessages(TMFMessage):
    """Log messages for create_service"""

    ERROR_FETCHING_SPEC = LogLevel.ERROR, "HTTP error fetching specification by id"
    ERROR_RETRIEVING_SPECIFICATION = (
        LogLevel.ERROR,
        "Error retrieving specification data",
    )
    SPEC_NOT_FOUND = LogLevel.ERROR, "Specification does not match name and version"
    SERVICE_TYPE_MODIFICATION = (
        LogLevel.INFO,
        "ServiceType does not match ServiceSpecification. Updating ServiceType.",
    )
    MISSING_SPECIFICATION_INFORMATION = (
        LogLevel.ERROR,
        "Missing information to get service specification from catalog api",
    )
