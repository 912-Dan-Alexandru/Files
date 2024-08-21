"""
TMF Service Model
"""
from pydantic import BaseModel


class DisableInitialPopulation(BaseModel):
    """
    Model for inventory-agent:disable-initial-population
    """

    velocloud: bool = False
    meraki: bool = False
    mist: bool = False
    fortimanager: bool = False

    def __bool__(self):
        """Return True if all the inner values are True"""
        return self.velocloud and self.meraki and self.mist and self.fortimanager

    def __or__(self, other):
        """Allow us to combine two with |"""
        if isinstance(other, DisableInitialPopulation):
            return DisableInitialPopulation(
                velocloud=self.velocloud or other.velocloud,
                meraki=self.meraki or other.meraki,
                mist=self.mist or other.mist,
                fortimanager=self.fortimanager or other.fortimanager,
            )
        raise ValueError(f"Object is not of type ${type(self)}")

    def override_population_enabled(
        self,
        velocloud_populate: bool,
        meraki_populate: bool,
        mist_populate: bool,
        fortimanager_populate: bool,
    ):
        """
        If Disable Initial Population is True or population is Enabled
        There will be no change.
        If Disable Initial Population is False and population is Disabled
        Then we need to mark the Initial Population must be Disabled.
        """
        return DisableInitialPopulation(
            velocloud=self.velocloud or not velocloud_populate,
            meraki=self.meraki or not meraki_populate,
            mist=self.mist or not mist_populate,
            fortimanager=self.fortimanager or not fortimanager_populate,
        )
