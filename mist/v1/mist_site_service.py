"""
Mist V1 API Calls: MSP site
"""
from .mist import SBMistV1
from .models import MistSiteV1


def get_mist_organization_sites(client: SBMistV1, org_id: str) -> list[MistSiteV1]:
    """
    API: /orgs/{{org_id}}/sites
    Raises:
        `httpx.HTTPError`
        `pydantic.ValidationError`
    """
    return client.get_api(f"/orgs/{org_id}/sites", list[MistSiteV1])
