"""
Velocloud V1 Configuration/Profiles API Calls
"""

from common.parsing import evaluate_model
from common.southbound.velocloud.v1.models.profiles.profile_configuration import (
    VelocloudProfileConfigurationUpdate,
)
from common.southbound.velocloud.v1.models.profiles.profile_module import (
    ConfigurationModule,
)

from . import models
from .velocloud import SBVelocloudV1


def get_enterprise_configuration_profiles(
    client: SBVelocloudV1, enterprise_id
) -> list[models.VelocloudProfileConfiguration]:
    """
    API: /enterprise/getEnterpriseConfigurations"

    Fetches available profiles/configurations  for a given enterprise
    """
    data = client.post_api(
        endpoint="/enterprise/getEnterpriseConfigurations",
        body={
            "enterpriseId": enterprise_id,
            "with": ["edgeCount", "modules"],
        },
    )
    return evaluate_model(list[models.VelocloudProfileConfiguration], data)


def get_enterprise_configuration_profile(
    client: SBVelocloudV1, enterprise_id: int, configuration_id: int
) -> models.VelocloudProfileConfiguration:
    """
    API: /configuration/getConfiguration

    Gets the specified configuration profile, optionally with module details.
    Possible option: [ modules, edgeCount, enterprises, enterpriseCount, counts ]
    """
    body = {
        "with": ["enterpriseCount", "modules", "edgeCount"],
        "enterpriseId": enterprise_id,
        "id": configuration_id,
    }

    data = client.post_api(endpoint="/configuration/getConfiguration", body=body)
    return evaluate_model(models.VelocloudProfileConfiguration, data)


def get_enterprise_configuration_profile_modules(
    client: SBVelocloudV1, enterprise_id: int, configuration_id: int
) -> list[ConfigurationModule]:
    """
    API: /configuration/getConfigurationModules

    Gets all configuration modules for the specified configuration profile.

    Possible modules option: imageUpdate, controlPlane, managementPlane, firewall,
    QOS, deviceSettings, WAN, metaData, properties, analyticsSettings, atpMetadata.
    """
    body = {
        "configurationId": configuration_id,
        "enterpriseId": enterprise_id,
        "noData": False,
        "modules": [
            "imageUpdate",
            "controlPlane",
            "managementPlane",
            "firewall",
            "QOS",
            "deviceSettings",
            "WAN",
            "metaData",
            "properties",
            "analyticsSettings",
            "atpMetadata",
        ],
    }

    data = client.post_api(endpoint="/configuration/getConfigurationModules", body=body)
    return evaluate_model(
        list[ConfigurationModule],
        data,
    )


def create_enterprise_configuration_profile(
    client: SBVelocloudV1,
    configuration_profile: models.ConfigurationCloneEnterpriseTemplate,
) -> models.ConfigurationCloneEnterpriseTemplateResult:
    """
    API: /configuration/cloneEnterpriseTemplate

    Creates a new enterprise configuration from the enterprise default configuration.
    On success, returns the id of the newly created configuration object.
    """

    data = client.post_api(
        endpoint="/configuration/cloneEnterpriseTemplate",
        body=configuration_profile.dict(exclude_unset=True, by_alias=True),
    )
    return evaluate_model(models.ConfigurationCloneEnterpriseTemplateResult, data)


def delete_enterprise_configuration_profile(
    client: SBVelocloudV1,
    delete_configuration: models.ConfigurationDeleteConfiguration,
) -> models.EntityStateChangeOutcomeConfirmation:
    """
    API: /configuration/deleteConfiguration
    Deletes the specified configuration profile (by id).
    On success, returns an object indicating the number of
    objects (rows) deleted (1 or 0).
    """

    data = client.post_api(
        endpoint="/configuration/deleteConfiguration",
        body=delete_configuration.dict(exclude_unset=True, by_alias=True),
    )
    return evaluate_model(models.EntityStateChangeOutcomeConfirmation, data)


def update_enterprise_configuration_profile(
    client: SBVelocloudV1,
    enterprise_id: int,
    updated_configuration: VelocloudProfileConfigurationUpdate,
) -> models.EntityStateChangeOutcomeConfirmation:
    """
    API: /configuration/updateConfiguration
    Updates the specified configuration profile record values such as:
    "name","description","version","effective"
    """
    body = {
        "enterpriseId": enterprise_id,
        "id": updated_configuration.id,
        "_update": updated_configuration.dict(
            by_alias=True, exclude_unset=True, exclude={"id"}
        ),
    }

    data = client.post_api(endpoint="/configuration/updateConfiguration", body=body)
    return evaluate_model(models.EntityStateChangeOutcomeConfirmation, data)


def update_enterprise_configuration_module(
    client: SBVelocloudV1,
    enterprise_id: int,
    updated_configuration_module: ConfigurationModule,
) -> models.EntityStateChangeOutcomeConfirmation:
    """
    API: /configuration/updateConfigurationModule

    Updates the specified configuration module and/or modifies
    its network service associations (refs). Example use cases include:

    Create a new firewall rule or modify an existing one
    Create a business policy or modify an existing one
    Configure device settings such as high availability, Cloud VPN, etc.
    """
    body = {
        "enterpriseId": enterprise_id,
        "configurationModuleId": updated_configuration_module.id,
        "_update": updated_configuration_module.dict(
            by_alias=True,
            exclude_unset=True,
            exclude={"id", "type", "created", "configuration_id"},
        ),
    }

    data = client.post_api(
        endpoint="/configuration/updateConfigurationModule", body=body
    )
    return evaluate_model(models.EntityStateChangeOutcomeConfirmation, data)
