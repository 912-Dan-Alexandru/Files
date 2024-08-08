"""
Mist V1 API Calls
/msps Endpoint
"""
from .mist import SBMistV1
from .models import MistMSPV1, MistOrganizationGroupV1, MistOrganizationV1


def get_msp_info(client: SBMistV1, msp_id: str) -> MistMSPV1:
    """
    API: /msps/{msp_id}
    Raises:
        `httpx.HTTPError`
        `pydantic.ValidationError`
    """
    return client.get_api(f"/msps/{msp_id}", MistMSPV1)


def get_msp_orgs(client: SBMistV1, msp_id: str) -> list[MistOrganizationV1]:
    """
    API: /msps/{msp_id}/orgs
    Raises:
        `httpx.HTTPError`
        `pydantic.ValidationError`
    """
    return client.get_api(f"/msps/{msp_id}/orgs", list[MistOrganizationV1])


def get_msp_org_groups(client: SBMistV1, msp_id: str) -> list[MistOrganizationGroupV1]:
    """
    API: /msps/{msp_id}/orggroups
    Raises:
        `httpx.HTTPError`
        `pydantic.ValidationError`
    """
    return client.get_api(f"/msps/{msp_id}/orggroups", list[MistOrganizationGroupV1])
