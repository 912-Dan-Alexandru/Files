"""
Mist V1 API Calls
/orgs Endpoint
"""
from .mist import SBMistV1
from .models import MistOrganizationV1


def get_org_info(client: SBMistV1, org_id: str) -> MistOrganizationV1:
    """
    API: /orgs/{org_id}
    Raises:
        `httpx.HTTPError`
        `pydantic.ValidationError`
    """
    return client.get_api(f"/orgs/{org_id}", MistOrganizationV1)
