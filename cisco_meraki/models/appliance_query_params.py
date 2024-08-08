"""
Appliance config pydantic model
"""


from pydantic import BaseModel, Field


class UplinksStatusesQueryParams(BaseModel):
    """
    get_appliance_uplinks_statuses configurable params.
    REF:
    https://developer.cisco.com/meraki/api-v1/get-organization-appliance-uplink-statuses/
    """

    per_page: int | None = Field(
        alias="perPage",
        description=(
            "The number of entries per page returned. "
            "Acceptable range is 3 - 1000. Meraki default is 1000."
        ),
        default=None,
    )
    starting_after: str | None = Field(
        alias="startingAfter",
        description=(
            "A token used by the server to indicate the start of the page. Often this "
            "is a timestamp or an ID but it is not limited to those. This parameter "
            "should not be defined by client applications. The link for the first, "
            "last, prev, or next page in the HTTP Link header should define it."
        ),
        default=None,
    )
    ending_before: str | None = Field(
        alias="endingBefore",
        description=(
            "A token used by the server to indicate the end of the page. Often this is"
            "a timestamp or an ID but it is not limited to those. This parameter should"
            " not be defined by client applications. The link for the first, last, "
            "prev, or next page in the HTTP Link header should define it."
        ),
        default=None,
    )
    serials: list[str] | None = Field(
        description=(
            "A list of serial numbers. The returned devices will be filtered to only "
            "include these serials."
        ),
        default=None,
    )
    network_ids: list[str] | None = Field(
        alias="networkIds",
        description=(
            "A list of network IDs. The returned devices will be filtered to only "
            "include these networks."
        ),
        default=None,
    )
    iccids: list[str] | None = Field(
        description=(
            "A list of ICCIDs. The returned devices will be filtered to only include "
            "these ICCIDs."
        ),
        default=None,
    )


class UplinksUsageByNetworkQueryParams(BaseModel):
    """
    get_organization_appliance_uplinks_usage_byNetwork
    REF:
    https://developer.cisco.com/meraki/api-latest/get-organization-appliance-uplinks-usage-by-network/
    """

    t0: str | None = Field(
        alias="t0",
        description=(
            "The beginning of the timespan for the data."
            "The maximum lookback period is 365 days from today."
        ),
        default=None,
    )
    t1: str | None = Field(
        alias="t1",
        description=(
            "The end of the timespan for the data."
            "t1 can be a maximum of 14 days after t0."
        ),
        default=None,
    )
    timespan: int | None = Field(
        alias="timespan",
        description=(
            "The timespan for which the information will be fetched."
            "If specifying timespan, do not specify parameters t0 and t1."
            "The value must be in seconds and be less than or equal to 14 days."
            "The default is 1 day."
        ),
        default=None,
    )


class VpnStatsQueryParams(BaseModel):
    """
    get_organization_appliance_vpn_stats
    REF:
    https://developer.cisco.com/meraki/api-v1/get-organization-appliance-vpn-stats/
    """

    per_page: int | None = Field(
        alias="perPage",
        description=(
            "The number of entries per page returned. "
            "Acceptable range is 3 - 1000. Meraki default is 1000."
        ),
        default=None,
    )
    starting_after: str | None = Field(
        alias="startingAfter",
        description=(
            "A token used by the server to indicate the start of the page. Often this "
            "is a timestamp or an ID but it is not limited to those. This parameter "
            "should not be defined by client applications. The link for the first, "
            "last, prev, or next page in the HTTP Link header should define it."
        ),
        default=None,
    )
    ending_before: str | None = Field(
        alias="endingBefore",
        description=(
            "A token used by the server to indicate the end of the page. Often this is"
            "a timestamp or an ID but it is not limited to those. This parameter should"
            " not be defined by client applications. The link for the first, last, "
            "prev, or next page in the HTTP Link header should define it."
        ),
        default=None,
    )
    network_ids: list[str] | None = Field(
        alias="networkIds",
        description=(
            "A list of network IDs. The returned devices will be filtered to only "
            "include these networks."
        ),
        default=None,
    )
    t0: str | None = Field(
        alias="t0",
        description=(
            "The beginning of the timespan for the data"
            "The maximum lookback period is 365 days from today."
        ),
        default=None,
    )
    t1: str | None = Field(
        alias="t1",
        description=(
            "The end of the timespan for the data."
            "t1 can be a maximum of 14 days after t0."
        ),
        default=None,
    )
    timespan: int | None = Field(
        alias="timespan",
        description=(
            "The timespan for which the information will be fetched"
            "If specifying timespan, do not specify parameters t0 and t1."
            "The value must be in seconds and be less than or equal to 14 days."
            "The default is 1 day."
        ),
        default=None,
    )


class UplinksLossAndLatencyQueryParams(BaseModel):
    """
    get organization appliance vpn stats
    REF: https://developer.cisco.com/meraki/api-v1/
            get-organization-devices-uplinks-loss-and-latency/

    """

    uplinkstring: list[str] | None = Field(
        alias="uplinkstring",
        description=(
            "Optional filter for a specific WAN uplink."
            "Valid uplinks are wan1, wan2, wan3, cellular."
            "Default will return all uplinks."
        ),
        default=None,
    )
    ip: str | None = Field(
        alias="ip",
        description=(
            "Optional filter for a specific destination IP."
            "Default will return all destination IPs."
        ),
        default=None,
    )
    t0: str | None = Field(
        alias="t0",
        description=(
            "The beginning of the timespan for the data."
            "The maximum lookback period is 60 days from today."
        ),
        default=None,
    )
    t1: str | None = Field(
        alias="t1",
        description=(
            "The end of the timespan for the data. "
            "t1 can be a maximum of 5 minutes after t0."
            "The latest possible time that t1 can be is 2 minutes into the past."
        ),
        default=None,
    )
    timespan: int | None = Field(
        alias="timespan",
        description=(
            "The timespan for which the information will be fetched."
            "If specifying timespan, do not specify parameters t0 and t1."
            "The value must be in seconds and be less than or equal to 5 minutes."
            "The default is 5 minutes."
        ),
        default=None,
    )
