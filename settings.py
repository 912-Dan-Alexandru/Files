"""
Inventory Agent Config Model
"""

from functools import lru_cache
from typing import Literal

from pydantic import parse_obj_as

from common.config import ConfigLoader
from common.database.redis import RedisDB
from common.models.settings import (
    ConfigCelerySettings,
    ConfigFortiManager,
    ConfigFortiManagerClient,
    ConfigMeraki,
    ConfigMist,
    ConfigSchedulerSettings,
    ConfigTMFServicesSettings,
    ConfigVelocloud,
    VelocloudConfigMap,
)
from common.resources import ResourceType
from common.southbound.cisco_meraki import SBMeraki
from common.southbound.fortimanager.v1.fortimanager import SBFortiManagerV1
from common.southbound.mist.v1.mist import SBMistV1
from common.southbound.velocloud import SBVelocloudV1, v1
from common.tools import TMFLogger

from .messages import ConfigMessages as Messages

VENDORS = ("MIST", "MERAKI", "VELOCLOUD", "FORTIMANAGER")


class InventoryAgentSettings(
    ConfigCelerySettings, ConfigTMFServicesSettings, ConfigSchedulerSettings
):
    """Inventory Agent Config Settings"""


def get_queue_routes():
    """
    Gets the routes in a dictionary
    """
    return {
        "velocloud*": "VELOCLOUD",
        "meraki*": "MERAKI",
        "mist*": "MIST",
        "forti*": "FORTIMANAGER",
        "common.scheduler.*": "SchedulerController",
        "common.readiness.*": "celery",
    }


@lru_cache
def get_config() -> ConfigLoader:
    """
    Get the config inventory agent
    """
    return ConfigLoader("inventory_agent/config.yml", extended_substitution=False)


@lru_cache
def get_settings():
    """
    Get the settings for the API
    """
    return InventoryAgentSettings(**get_config().config)


def get_tmf_settings():
    """
    Get the tmf services settings
    """
    return ConfigTMFServicesSettings(**get_config().config).tmf_services


def service_inventory_base_url() -> str:
    """
    Get the Service Inventory Base Url
    """
    return str(get_tmf_settings().service_inventory)


def service_catalog_base_url() -> str:
    """
    Get the Service Inventory Base Url
    """
    return str(get_tmf_settings().service_catalog)


def get_celery_settings():
    """
    Get the celery settings
    """
    return ConfigCelerySettings(**get_config().config).celery


@lru_cache
def get_scheduler_settings():
    """
    Get the celery settings
    """
    return ConfigSchedulerSettings(**get_config().config).sync_wave_scheduler.crontab


@lru_cache
def get_enabled_vendors() -> (
    tuple[Literal["MIST", "MERAKI", "VELOCLOUD", "FORTIMANAGER"], ...]
):
    """
    Get the vendors from the Vendors class as a List
    """
    return tuple(
        filter(lambda v: bool(get_config().get_bool(v.lower(), "populate")), VENDORS)
    )


@lru_cache
def get_redis_broker():
    """
    Get the redis broker
    """
    return RedisDB(uri=get_celery_settings().broker)


@lru_cache
def get_velocloud() -> tuple[list[SBVelocloudV1], list[VelocloudConfigMap]]:
    """
    Get Velocloud Client
    Raises:
        ValidationError: If velocloud config does not conform to ConfigVelocloud
        ValueError: if multi-vco config items don't contain the same number of values
    """

    velocloud_config = parse_obj_as(ConfigVelocloud, get_config().config["velocloud"])
    hosts = velocloud_config.url.split("::")
    verify_ssls = (
        [velocloud_config.verify_ssl]
        if isinstance(velocloud_config.verify_ssl, bool)
        else [
            i in ["true", "True", True] for i in velocloud_config.verify_ssl.split("::")
        ]
    )
    zip_vco = zip(velocloud_config.token.split("::"), hosts, verify_ssls)
    velocloud = [
        SBVelocloudV1(host=url, api_key=token, verify_ssl=verify_ssl, vco_index=index)
        for index, (token, url, verify_ssl) in enumerate(zip_vco, start=1)
    ]
    velocloud_config_maps = [
        VelocloudConfigMap(
            token=velo_client.api_key
            if isinstance(velo_client.api_key, str)
            else velo_client.api_key(),
            url=velo_client.host,
            vco_index=str(velo_client.vco_index),
            msp_name=msp.name,
            msp_velo_id=msp.id,
            msp_inv_id=ResourceType.MEF_MSP.get_resource_hex(
                msp.id, velo_client.vco_index
            ),
            verify_ssl=velo_client.verify_ssl,
        )
        for (velo_client, msp) in [
            (velo_client, v1.enterprise_proxy.get_enterprise_proxy(velo_client))
            for velo_client in velocloud
        ]
    ]
    TMFLogger().log(Messages.VELOCLOUD_CONFIGURED, velocloud_clients=velocloud)
    return velocloud, velocloud_config_maps


def get_meraki_config() -> ConfigMeraki:
    """
    Get Meraki Config
    """
    return ConfigMeraki.parse_obj(get_config().config["meraki"])


@lru_cache
def get_meraki() -> SBMeraki:
    """
    Get Meraki Client Configuration
    """
    meraki_config = get_meraki_config()
    TMFLogger().log(Messages.MERAKI_CONFIGURED, population=meraki_config.populate)
    return SBMeraki(meraki_config.endpoint, meraki_config.token)


@lru_cache
def get_mist() -> SBMistV1:
    """
    Get Mist Client
    """
    mist_config = parse_obj_as(ConfigMist, get_config().config["mist"])
    TMFLogger().log(Messages.MIST_CONFIGURED, population=mist_config.populate)
    return SBMistV1(mist_config.url, mist_config.token)


@lru_cache
def get_fortimanager() -> list[SBFortiManagerV1]:
    """
    Get FortiManager Clients
    """
    fortimanager_configs = ConfigFortiManager(
        populate=get_config().get_bool("fortimanager", "populate") or False,
        clients=parse_obj_as(
            list[ConfigFortiManagerClient],
            get_config().get_list("fortimanager", "clients"),
        ),
    )

    fortimanager_clients = [
        SBFortiManagerV1(
            host=config.url,
            username=config.username,
            password=config.password,
            verify_ssl=config.verify_ssl,
        )
        for config in fortimanager_configs.clients
    ]

    return fortimanager_clients
