"""
Mist V1 API Calls: Mist account configuration and privileges
"""
from .mist import SBMistV1
from .models import MistAccountModelV1


def get_account_settings(client: SBMistV1) -> MistAccountModelV1:
    """
    API: GET /self
    Raises:
        `httpx.HTTPError`
        `pydantic.ValidationError`
    """
    return client.get_api("/self", MistAccountModelV1)
