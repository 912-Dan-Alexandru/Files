"""
FortiManager Device V1 Pydantic models
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Extra, Field, validator


class ConfStatusEnum(str, Enum):
    """
    Configuration states
    """

    UNKNOWN = "unknown"
    INSYNC = "insync"
    OUTOFSYNC = "outofsync"


class ConnModeEnum(str, Enum):
    """
    Connection mode
    """

    ACTIVE = "active"
    PASSIVE = "passive"


class ConnStatusEnum(str, Enum):
    """
    Connection states
    """

    UNKNOWN = "UNKNOWN"
    UP = "up"
    DOWN = "down"


class DbStatusEnum(str, Enum):
    """
    Database states
    """

    UNKNOWN = "unknown"
    NOMOD = "nomod"
    MOD = "mod"


class DevStatusEnum(str, Enum):
    """
    Device states
    """

    NONE = "none"
    UNKNOWN = "unknown"
    CHECKEDIN = "checkedin"
    INPROGRESS = "inprogress"
    INSTALLED = "installed"
    ABORTED = "aborted"
    SCHED = "sched"
    RETRY = "retry"
    CANCELED = "canceled"
    PENDING = "pending"
    RETRIEVED = "retrieved"
    CHANGED_CONF = "changed_conf"
    SYNC_FAIL = "sync_fail"
    TIMEOUT = "timeout"
    REV_REVERT = "rev_revert"
    AUTO_UPDATED = "auto_updated"


class FosLicDrSiteEnum(str, Enum):
    """
    VM Meter DR Site states
    """

    DISABLE = "disable"
    ENABLE = "enable"


class FosLicTypeEnum(str, Enum):
    """
    VM Meter license types
    """

    TEMPORARY = "temporary"
    TRIAL = "trial"
    REGULAR = "regular"
    TRIAL_EXPIRED = "trial_expired"


class FosLicUtmEnum(str, Enum):
    """
    VM Meter services
    """

    FW = "fw"
    AV = "av"
    IPS = "ips"
    APP = "app"
    URL = "url"
    UTM = "utm"
    FWB = "fwb"


class HaModeEnum(str, Enum):
    """
    High Availability mode
    """

    STANDALONE = "standalone"
    AP = "AP"
    AA = "AA"
    ELBC = "ELBC"
    DUAL = "DUAL"
    FMG_ENABLED = "fmg-enabled"
    AUTOSCALE = "autoscale"
    UNKNOWN = "unknown"


class RoleEnum(str, Enum):
    """
    Device roles
    """

    MASTER = "master"
    HA_SLAVE = "ha-slave"
    AUTOSCALE_SLAVE = "autoscale-slave"


class VmStatusEnum(str, Enum):
    """
    VM states
    """

    N_A = "N/A"
    NO_LICENSE = "No License"
    STARTUP = "Startup"
    VALID = "Valid"
    PENDING = "Pending"
    WARNING = "Warning"
    INVALID = "Invalid"
    INVALID_COPY = "Invalid Copy"
    EVALUATION_EXPIRED = "Evaluation Expired"
    EVALUATION = "Evaluation"
    EXPIRES_SOON = "Expires Soon"
    EXPIRED = "Expired"
    GRACE_PERIOD = "Grace Period"
    VALIDATION_OVERDUE = "Validation Overdue"


class FlagsEnum(str, Enum):
    """
    flags
    """

    HAS_HDD = "has_hdd"
    VDOM_ENABLED = "vdom_enabled"
    DISCOVER = "discover"
    RELOAD = "reload"
    INTERIM_BUILD = "interim_build"
    OFFLINE_MODE = "offline_mode"
    BACKUP_MODE = "backup_mode"
    IS_MODEL = "is_model"
    FIPS_MODE = "fips_mode"
    LINKED_TO_MODEL = "linked_to_model"
    IP_CONFLICT = "ip_conflict"
    FAZ_AUTOSYNC = "faz-autosync"
    AZURE_VWAN_NVA = "azure_vwan_nva"
    FGSP_CONFIGURED = "fgsp_configured"
    NEED_RESET = "need_reset"
    CNF_MODE = "cnf_mode"
    SASE_MANAGED = "sase_managed"
    OVERRIDE_MANAGEMENT_INTF = "override_management_intf"


class VdomOpModeEnum(str, Enum):
    """
    vdom op mode
    """

    NAT = "nat"
    TRANSPARENT = "transparent"


class VdomStatusEnum(str, Enum):
    """
    VDOM states
    """

    TRAFFIC = "traffic"
    ADMIN = "admin"


class MgmtModeEnum(str, Enum):
    """
    Management mode
    """

    UNREG = "unreg"
    FMG = "fmg"
    FAZ = "faz"
    FMGFAZ = "fmgfaz"


class OsTypeEnum(str, Enum):
    """
    Operating system types
    """

    UNKNOWN = "unknown"
    FOS = "fos"
    FSW = "fsw"
    FOC = "foc"
    FML = "fml"
    FAZ = "faz"
    FWB = "fwb"
    FCH = "fch"
    FCT = "fct"
    LOG = "log"
    FMG = "fmg"
    FSA = "fsa"
    FDD = "fdd"
    FAC = "fac"
    FPX = "fpx"
    FNA = "fna"
    FFW = "ffw"
    FSR = "fsr"
    FAD = "fad"
    FDC = "fdc"
    FAP = "fap"
    FXT = "fxt"
    FTS = "fts"
    FAI = "fai"
    FWC = "fwc"
    FIS = "fis"
    FED = "fed"
    FPA = "fpa"
    FCA = "fca"
    FTC = "ftc"


class DeviceMetafields(BaseModel, extra=Extra.allow):
    """
    Meta Fields item model
    """

    underlay_circuit_reference: str | None = Field(None, alias="VF 3C Ref")
    address: str | None = Field(None, alias="Address")
    company_org: str | None = Field(None, alias="Company/Organization")
    email: str | None = Field(None, alias="Contact Email")
    phone_number: str | None = Field(None, alias="Contact Phone Number")
    custom_info: str | None = Field(None, alias="Custom_info ")
    order_ref: str | None = Field(None, alias="VF Order Ref")


class HaSlaveRoleEnum(str, Enum):
    """
    Ha slave roles enum
    """

    SLAVE = "slave"
    MASTER = "master"


class HaSlaveItem(BaseModel):
    """
    High availability Slave model
    """

    conf_status: int = Field(..., description="Configuration status.")
    idx: int = Field(..., description="Index.")
    name: str = Field(..., description="Name.")
    prio: int = Field(..., description="Priority.")
    role: HaSlaveRoleEnum = Field(HaSlaveRoleEnum.SLAVE, description="Role.")
    sn: str = Field(..., description="Serial number.")
    status: int = Field(..., description="Status.")
    did: str
    flags: list[FlagsEnum] | FlagsEnum | None = None


class OnboardRuleItem(BaseModel):
    """
    Onboard Rule object
    """

    adm_pass: list[str]
    adm_usr: str
    did: str
    flags: list[FlagsEnum] | FlagsEnum | None = None
    name: str
    sn: str
    type: str


class VdomItem(BaseModel):
    """
    VDOM model
    """

    comments: str | None = None
    meta_fields: dict[str, str] | None = Field(None, description="Meta fields.")
    opmode: VdomOpModeEnum | None = Field(
        VdomOpModeEnum.NAT, description="Operation mode."
    )
    rtm_prof_id: int = Field(..., description="RTM profile ID.")
    vdom_type: VdomStatusEnum | None = Field(
        VdomStatusEnum.TRAFFIC, description="Virtual domain type."
    )
    vpn_id: int = Field(..., description="VPN ID.")
    devid: str
    ext_flags: int
    flags: list[FlagsEnum] | FlagsEnum | None = None
    name: str
    status: Any


class FortiManagerDeviceV1(BaseModel):
    """
    FortiManager Device V1 model
    """

    adm_pass: list[str]
    adm_usr: str
    app_ver: str
    auto_mgmt: Any
    av_ver: str
    beta: int
    branch_pt: int
    build: int
    checksum: str
    conf_status: ConfStatusEnum = Field(
        ConfStatusEnum.UNKNOWN, description="Configuration status."
    )
    conn_mode: ConnModeEnum = Field(
        ConnModeEnum.PASSIVE, description="Connection mode."
    )
    conn_status: ConnStatusEnum = Field(
        ConnStatusEnum.UNKNOWN, description="Connection status."
    )
    db_status: DbStatusEnum = Field(
        DbStatusEnum.UNKNOWN, description="Database status."
    )
    desc: str
    dev_status: DevStatusEnum = Field(
        DevStatusEnum.UNKNOWN, description="Device status."
    )
    eip: str
    fap_cnt: int
    faz_full_act: int = Field(
        alias="faz.full_act", description="Full-Active sessions on FortiAnalyzer."
    )
    faz_perm: int = Field(alias="faz.perm", description="FortiAnalyzer permissions.")
    faz_quota: int = Field(alias="faz.quota", description="FortiAnalyzer quota.")
    faz_used: int = Field(alias="faz.used", description="FortiAnalyzer used space.")
    fex_cnt: int
    first_tunnel_up: int = Field(..., description="Time of first tunnel up.")
    flags: list[FlagsEnum] | FlagsEnum | None = Field(None, description="Flags.")
    foslic_cpu: int = Field(..., description="VM Meter vCPU count.")
    foslic_dr_site: FosLicDrSiteEnum = Field(
        FosLicDrSiteEnum.DISABLE, description="VM Meter DR Site status."
    )
    foslic_inst_time: int = Field(
        ..., description="VM Meter first deployment time (UNIX timestamp)."
    )
    foslic_last_sync: int = Field(
        ..., description="VM Meter last synchronized time (UNIX timestamp)."
    )
    foslic_ram: int = Field(..., description="VM Meter device RAM size (in MB).")
    foslic_type: FosLicTypeEnum = Field(
        FosLicTypeEnum.TEMPORARY, description="VM Meter license type."
    )
    foslic_utm: list[FosLicUtmEnum] | None = Field(
        ..., description="VM Meter services."
    )
    fsw_cnt: int = Field(..., description="FortiSwitch count.")
    ha_group_id: int = Field(..., description="High Availability group ID.")
    ha_group_name: str = Field(..., description="High Availability group name.")
    ha_mode: HaModeEnum = Field(
        HaModeEnum.STANDALONE, description="High Availability mode."
    )
    ha_slave: list[HaSlaveItem] | None = Field(
        ..., description="List of HA slave devices."
    )
    hdisk_size: int = Field(..., description="Hard disk size (in MB).")
    hostname: str = Field(..., description="Hostname.")
    hw_generation: int = Field(..., description="Hardware generation.")
    hw_rev_major: int = Field(..., description="Hardware revision major.")
    hw_rev_minor: int = Field(..., description="Hardware revision minor.")
    hyperscale: int = Field(..., description="Hyperscale count.")
    ip: str
    ips_ext: int = Field(..., description="IPS extended sessions.")
    ips_ver: str = Field(..., description="IPS version.")
    last_checked: int = Field(..., description="Last checked time.")
    last_resync: int
    latitude: str = Field(..., description="Latitude.")
    lic_flags: int = Field(..., description="License flags.")
    lic_region: str = Field(..., description="License region.")
    location_from: str = Field(..., description="Location from.")
    logdisk_size: int = Field(..., description="Log disk size (in MB).")
    longitude: str
    maxvdom: int = Field(10, description="Maximum number of virtual domains (vdoms).")
    meta_fields: DeviceMetafields | None = Field(default=None, alias="meta fields")
    mgmt_if: str
    mgmt_mode: MgmtModeEnum = Field(MgmtModeEnum.UNREG, description="Management mode.")
    mgmt_uuid: str
    mgt_vdom: str
    module_sn: str
    mr: int = Field(-1, description="Module revision.")
    name: str = Field(..., description="Unique name for the device.")
    nsxt_service_name: str
    os_type: OsTypeEnum = Field(
        OsTypeEnum.UNKNOWN, description="Operating system type."
    )
    os_ver: int

    @validator("os_ver", pre=True, allow_reuse=True)
    @classmethod
    def convert_os_ver(cls, v):
        """
        Method for converting string "7.0" to integer 7
        The pydantic validator must have cls as first argument not self
        So ignore if sonar says it is a code smell
        """
        str_ver = str(v).split(".", maxsplit=1)[0]
        try:
            return int(str_ver)
        except ValueError:
            return 0

    oid: int
    onboard_rule: list[OnboardRuleItem] | None = None
    patch: int
    platform_str: str
    prefer_img_ver: str
    prio: int = Field(..., description="Priority.")
    private_key: str = Field(..., description="Private key.")
    private_key_status: int
    psk: str = Field(..., description="Pre-shared key.")
    role: RoleEnum = Field("master", description="Device role.")
    sn: str
    tab_status: str
    tunnel_cookie: str
    tunnel_ip: str
    vdom: list[VdomItem] | None = None
    version: int = Field(..., description="Device version.")
    vm_cpu: int = Field(..., description="VM CPU count.")
    vm_cpu_limit: int = Field(..., description="VM CPU limit.")
    vm_lic_expire: int = Field(..., description="VM license expiration time.")
    vm_lic_overdue_since: int = Field(..., description="VM license overdue since.")
    vm_mem: int = Field(..., description="VM memory size (in MB).")
    vm_mem_limit: int = Field(..., description="VM memory limit (in MB).")
    vm_status: VmStatusEnum | None = Field(VmStatusEnum.N_A, description="VM status.")


class FortiManagerLicenses(BaseModel):
    """
    FortiManager license model
    """

    account: str | None = None
    address: str | None = None
    company: str | None = None
    contract_item: list[str] | None = None
    industry: Any | None = None
    rawdata: str | None = None
    serial: str


class DeviceActionEnum(str, Enum):
    """
    add device mode
    """

    ADD_MODEL = "add_model"
    PROMOTE_UNREG = "promote_unreg"


class FortiManagerAddDeviceV1(FortiManagerDeviceV1):
    """
    FortiManager Add Device V1 model
    """

    authorization_template: str = Field(
        alias="authorization template",
        description="Add model device only. Fabric Authorization Template to \
            auto-generate for the new model device upon creation.",
    )
    device_action: DeviceActionEnum = Field(
        "",
        alias="device action",
        description='Leave blank to add a real device. \
            "add_model" - add a model device. \
            "promote_unreg" - promote an unregistered device to be managed by \
                            FortiManager using information from the database.',
    )
    device_blueprint: str = Field(
        alias="device blueprint",
        description="Add model device only. Device blueprint to apply \
            to the new model device.",
    )


class FortiManagerModifyDeviceV1(BaseModel):
    """
    FortiManager Modify Device V1 model
    """

    id: str | None = None
    ha_slave: list[HaSlaveItem] | None = None

    adm_pass: list[str] | None = None
    adm_usr: str | None = None
    app_ver: str | None = None
    av_ver: str | None = None
    beta: int | None = None
    branch_pt: int | None = None
    build: int | None = None
    checksum: str | None = None
    conf_status: ConfStatusEnum | None = None
    conn_mode: ConnModeEnum | None = None
    conn_status: ConnStatusEnum | None = None
    db_status: DbStatusEnum | None = None
    desc: str | None = None
    dev_status: DevStatusEnum | None = None
    eip: str | None = None
    fap_cnt: int | None = None
    faz_full_act: int | None = None
    faz_perm: int | None = None
    faz_quota: int | None = None
    faz_used: int | None = None
    fex_cnt: int | None = None
    first_tunnel_up: int | None = None
    flags: list[FlagsEnum] | FlagsEnum | None = None
    foslic_cpu: int | None = None
    foslic_dr_site: str | None = None
    foslic_inst_time: int | None = None
    foslic_last_sync: int | None = None
    foslic_ram: int | None = None
    foslic_type: FosLicTypeEnum | None = None
    foslic_utm: list[FosLicUtmEnum] | None = None
    fsw_cnt: int | None = None
    ha_group_id: int | None = None
    ha_group_name: str | None = None
    ha_mode: HaModeEnum | None = None
    hdisk_size: int | None = None
    hostname: str | None = None
    hw_generation: int | None = None
    hw_rev_major: int | None = None
    hw_rev_minor: int | None = None
    hyperscale: int | None = None
    ip: str | None = None
    ips_ext: int | None = None
    ips_ver: str | None = None
    last_checked: int | None = None
    last_resync: int | None = None
    latitude: str | None = None
    lic_flags: int | None = None
    lic_region: str | None = None
    location_from: str | None = None
    logdisk_size: int | None = None
    longitude: str | None = None
    maxvdom: int | None = None
    meta_fields: DeviceMetafields | dict[str, str] | None = None
    mgmt_if: str | None = None
    mgmt_mode: MgmtModeEnum | None = None
    mgmt_uuid: str | None = None
    mgt_vdom: str | None = None
    module_sn: str | None = None
    mr: int | None = None
    name: str | None = None
    nsxt_service_name: str | None = None
    os_type: OsTypeEnum | None = None
    os_ver: int | None = None
    patch: int | None = None
    platform_str: str | None = None
    prefer_img_ver: str | None = None
    prio: int | None = None
    private_key: str | None = None
    private_key_status: int | None = None
    psk: str | None = None
    role: RoleEnum | None = None
    sn: str | None = None
    vdom: list[VdomItem] | None = None
    version: int | None = None
    vm_cpu: int | None = None
    vm_cpu_limit: int | None = None
    vm_lic_expire: int | None = None
    vm_lic_overdue_since: int | None = None
    vm_mem: int | None = None
    vm_mem_limit: int | None = None
    vm_status: VmStatusEnum | None = None

    @validator("os_ver", pre=True, allow_reuse=True)
    @classmethod
    def convert_os_ver(cls, v):
        """
        Method for converting string "7.0" to integer 7
        The pydantic validator must have cls as first argument not self
        So ignore if sonar says it is a code smell
        """
        str_ver = str(v).split(".", maxsplit=1)[0]
        try:
            return int(str_ver)
        except ValueError:
            return 0
