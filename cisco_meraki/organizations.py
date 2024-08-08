"""
Meraki API
/organizations Endpoint Functions
"""

from meraki.exceptions import APIError

from common.parsing import evaluate_model
from common.tools import TMFLogger

from . import models
from .cisco_meraki import SBMeraki
from .messages import MerakiMessages as Messages


@SBMeraki.exception_handler
def get_organizations(client: SBMeraki) -> list[models.Organization]:
    """
    API: /organizations
    """
    data = client.api.organizations.getOrganizations()
    return evaluate_model(list[models.Organization], data)


@SBMeraki.exception_handler
def get_organization(client: SBMeraki, org_id: str) -> models.Organization:
    """
    API: /organization
    """
    data = client.api.organizations.getOrganization(org_id)
    return evaluate_model(models.Organization, data)


@SBMeraki.exception_handler
def create_organization(
    client: SBMeraki, organization_base_info: models.BasicOrganizationInfo
) -> models.Organization:
    """
    Create a new organization.
    API: POST /organizations
    """
    data = client.api.organizations.createOrganization(
        name=organization_base_info.name, management=organization_base_info.management
    )
    return evaluate_model(models.Organization, data)


@SBMeraki.exception_handler
def update_organization(
    client: SBMeraki, organization_id: str, organization: models.OrganizationUpdate
) -> models.Organization:
    """
    Updates an existing organization.
    API: PUT/organizations/{organizationId}
    """
    data = client.api.organizations.updateOrganization(
        organizationId=organization_id, **organization.dict(exclude_none=True)
    )
    return evaluate_model(models.Organization, data)


@SBMeraki.exception_handler
def clone_organization(
    client: SBMeraki,
    organization_base_info: models.BasicOrganizationInfo,
    organization_id: str,
) -> models.Organization:
    """
    Create a new organization by cloning the addressed organization.

    API: POST/organizations/{organizationId}/clone

    Args:
        client (SBMeraki): Meraki client.
        organization_base_info (models.BasicOrganizationInfo): model containing
        the name for the new organization.
        organization_id (str): ID of the organization that will be cloned.

    Returns:
        models.Organization: a new complete Meraki organization

    """
    data = client.api.organizations.cloneOrganization(
        organizationId=organization_id, name=organization_base_info.name
    )
    return evaluate_model(models.Organization, data)


@SBMeraki.exception_handler
def get_networks(
    client: SBMeraki, org_id: str, total_pages: int = 100
) -> list[models.Network]:
    """
    API: /organizations/{organizationId}/networks
    """
    try:
        data = client.api.organizations.getOrganizationNetworks(
            org_id, total_pages=total_pages
        )
    except APIError as exc:
        if exc.status in [403, 404]:
            TMFLogger().log(Messages.MERAKI_NETWORK_NOT_EXIST)
            return []
        raise exc
    return evaluate_model(list[models.Network], data)


@SBMeraki.exception_handler
def get_organization_config_templates(
    client: SBMeraki, org_id: str
) -> list[models.ConfigurationTemplate]:
    """
    API: /organizations/{organizationId}/configTemplates
    """
    try:
        data = client.api.organizations.getOrganizationConfigTemplates(
            organizationId=org_id
        )
    except APIError as exc:
        if exc.status in [403, 404]:
            TMFLogger().log(Messages.CONFIG_TEMPLATES, exc_info=True)
            return []
        raise exc
    return evaluate_model(list[models.ConfigurationTemplate], data)


@SBMeraki.exception_handler
def get_devices(
    client: SBMeraki, org_id: str, total_pages: int = 100
) -> list[models.OrganizationDevice]:
    """
    API: /organizations/{organizationId}/devices
    """
    try:
        data = client.api.organizations.getOrganizationDevices(
            org_id, total_pages=total_pages
        )
    except APIError as exc:
        if exc.status in [403, 404]:
            TMFLogger().log(Messages.DEVICE_NOT_EXISTS, exc_info=True)
            return []
        raise exc
    return evaluate_model(list[models.OrganizationDevice], data)


@SBMeraki.exception_handler
def get_device_statuses(
    client: SBMeraki, org_id: str, serials
) -> list[models.OrganizationDevicesStatuses]:
    """
    API: /organizations/{organizationId}/devices/statuses
    """
    data = client.api.organizations.getOrganizationDevicesStatuses(
        org_id, serials=serials
    )
    return evaluate_model(list[models.OrganizationDevicesStatuses], data)


@SBMeraki.exception_handler
def get_uplinks_statuses(
    client: SBMeraki, org_id, serials
) -> list[models.OrganizationUplinksStatuses]:
    """
    API: /organizations/{organizationId}/uplinks/statuses
    """
    data = client.api.organizations.getOrganizationUplinksStatuses(
        org_id, serials=serials
    )
    return evaluate_model(list[models.OrganizationUplinksStatuses], data)


@SBMeraki.exception_handler
def get_inventory_device(
    client: SBMeraki, org_id: str, serial: str
) -> models.OrganizationInventoryDevice:
    """
    API: /organizations/{organizationId}/inventory/devices
    """
    data = client.api.organizations.getOrganizationInventoryDevice(org_id, serial)
    return evaluate_model(models.OrganizationInventoryDevice, data)


@SBMeraki.exception_handler
def create_network(
    client: SBMeraki, org_id: str, network_data: models.NetworkCreate
) -> models.Network:
    """
    API: POST /organizations/{organizationId}/networks
    """
    data = client.api.organizations.createOrganizationNetwork(
        organizationId=org_id, **network_data.dict(exclude_none=True)
    )
    return evaluate_model(models.Network, data)


@SBMeraki.exception_handler
def get_device_statuses_by_start_time(
    client: SBMeraki,
    org_id: str,
    serials,
    start_time: str,
    per_page: int,
) -> list[models.OrganizationDevicesStatuses]:
    """
    API: /organizations/{organizationId}/devices/statuses
    """
    data = client.api.organizations.getOrganizationDevicesStatuses(
        org_id,
        serials=serials,
        startingAfter=start_time,
        perPage=per_page,
        total_pages=-1,
    )
    return evaluate_model(list[models.OrganizationDevicesStatuses], data)


@SBMeraki.exception_handler
def get_uplinks_statuses_by_start_time(
    client: SBMeraki,
    org_id,
    serials,
    start_time: str,
    per_page: int,
) -> list[models.OrganizationUplinksStatuses]:
    """
    API: /organizations/{organizationId}/uplinks/statuses
    """
    data = client.api.organizations.getOrganizationUplinksStatuses(
        org_id,
        serials=serials,
        startingAfter=start_time,
        perPage=per_page,
        total_pages=-1,
    )
    return evaluate_model(list[models.OrganizationUplinksStatuses], data)


@SBMeraki.exception_handler
def claim_into_organization_inventory(
    client: SBMeraki,
    org_id: str,
    payload: models.InventoryItem,
) -> models.InventoryItem:
    """
    API: POST /organizations/{organizationId}/inventory/claim
    """
    data = client.api.organizations.claimIntoOrganizationInventory(
        org_id, **payload.dict(by_alias=True, exclude_none=True)
    )
    return evaluate_model(models.InventoryItem, data)


@SBMeraki.exception_handler
def release_from_organization_inventory(
    client: SBMeraki,
    org_id: str,
    device_serials: models.InventoryDeviceSerials,
) -> models.InventoryDeviceSerials:
    """
    API: POST /organizations/{organizationId}/inventory/release
    """
    data = client.api.organizations.releaseFromOrganizationInventory(
        org_id, **device_serials.dict(by_alias=True)
    )
    return evaluate_model(models.InventoryDeviceSerials, data)


@SBMeraki.exception_handler
def get_security_intrusion(
    client: SBMeraki,
    org_id,
) -> models.OrganizationIntrusionRules:
    """
    API: /organizations/{organizationId}/appliance/security/intrusion
    """
    data = client.api.appliance.getOrganizationApplianceSecurityIntrusion(org_id)
    return evaluate_model(models.OrganizationIntrusionRules, data)


@SBMeraki.exception_handler
def update_security_intrusion(
    client: SBMeraki,
    org_id,
    rules: models.OrganizationIntrusionRules,
) -> models.OrganizationIntrusionRules:
    """
    API: /organizations/{organizationId}/appliance/security/intrusion
    """
    paramlist: list = []
    for i in rules.allowedRules:
        paramlist.append({"ruleId": i.ruleId, "message": i.message})
    data = client.api.appliance.updateOrganizationApplianceSecurityIntrusion(
        org_id, paramlist
    )
    return evaluate_model(models.OrganizationIntrusionRules, data)
