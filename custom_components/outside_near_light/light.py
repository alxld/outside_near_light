"""Platform for light integration"""
from __future__ import annotations
import sys
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

sys.path.append("custom_components/new_light")
from new_light import NewLight


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the light platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    ent = OutsideNearLight()
    add_entities([ent])


class OutsideNearLight(NewLight):
    """Outside Near Light."""

    def __init__(self) -> None:
        """Initialize Outside Near Light."""
        super(OutsideNearLight, self).__init__(
            "Outside Near", domain=DOMAIN, debug=False, debug_rl=False
        )

        self.entities["light.outside_near_group"] = None
        self.switch = "Outside Switch"

        self.other_light_trackers["light.outside_group"] = -1
        self.track_other_light_off_events = True
