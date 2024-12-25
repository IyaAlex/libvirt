"""Support for wake on lan."""
import logging
import platform
import subprocess as sp

import voluptuous as vol
import libvirt

from homeassistant.components.switch import PLATFORM_SCHEMA, SwitchEntity
from homeassistant.const import (
    CONF_NAME, CONF_URL
)
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.script import Script

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_URL): cv.string,
        vol.Required(CONF_NAME): cv.string
    }
)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up a libvirt switch."""
    url = config[CONF_URL]
    name = config[CONF_NAME]

    add_entities(
        [
            LibvirtSwitch(
                hass,
                name,
                url
            )
        ],
        True,
    )


class LibvirtSwitch(SwitchEntity):
    """Representation of a libvirt switch."""

    def __init__(
        self,
        hass,
        name,
        url
    ):
        """Initialize the WOL switch."""
        self._hass = hass
        self._name = name
        self._url = url
        self._state = False

    @property
    def is_on(self):
        """Return true if switch is on."""
        return self._state

    @property
    def name(self):
        """Return the name of the switch."""
        return self._name

    def turn_on(self):
        """Turn the device on."""
        _LOGGER.info(
            ""
        )

        # Try to connect
        conn = libvirt.open(self._url)

        # If connected get status
        if conn != None:
            domain = conn.lookupByName(self._name)
            domain.create()


    def turn_off(self):
        """Turn the device off if an off action is present."""
        _LOGGER.info(
            ""
        )

        # Try to connect
        conn = libvirt.open(self._url)

        # If connected get status
        if conn != None:
            domain = conn.lookupByName(self._name)
            domain.shutdown()

    def update(self):
        result = 0

        try:
            # Try to connect
            conn = libvirt.open(self._url)

            # If connected get status
            if conn != None:
                domain = conn.lookupByName(self._name)
                result = domain.isActive()

            self._state = bool(result)
        
        except:
            self._state = bool(result)
