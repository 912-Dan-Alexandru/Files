"""
Exception classes that can be thrown by the Cisco Meraki southbound client.
"""
from common.southbound.exceptions import (
    ClientError,
    ResourceNotFoundError,
    RateLimitError,
    ServerError,
    PermissionsError,
    UnknownError,
)


class NoAPIKeyError(ClientError):
    """
    Meraki SDK needs an API Key to make requests
    """


class BadRequestError(ClientError):
    """
    The request was unacceptable, often due to missing a required parameter.
    HTTP 400
    """


class ValidationError(ClientError):
    """
    Error validating API Response
    """


class UnauthorizedError(PermissionsError):
    """
    Incorrect API key
    HTTP 401
    """


class ForbiddenError(PermissionsError):
    """
    You don't have permissions to do that.
    HTTP 403
    """


class NotFoundError(ResourceNotFoundError):
    """
    The requested resource doesn't exist.
    HTTP 404
    """


class TooManyRequestsError(RateLimitError):
    """
    Too many requests hit the API too quickly.
    HTTP 429
    """


class InternalServerError(ServerError):
    """
    Meraki was unable to process the request.
    HTTP 500, 502, 503, 504
    """


class MerakiUnknownError(UnknownError):
    """
    An unexpected HTTP status code was returned
    """
