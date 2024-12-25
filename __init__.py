"""Support for start and shutdown libvirt virual machine."""
from functools import partial
import logging

import voluptuous as vol
import libvirt

from homeassistant.const import CONF_NAME, CONF_URL
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DOMAIN = "libvirt"

SERVICE_START_DOM_LIBVIRT = "start_dom_libvirt"
SERVICE_RUNNING_DOM_LIBVIRT = "running_dom_libvirt"
SERVICE_SHUTDOWN_DOM_LIBVIRT = "shutdown_dom_libvirt"

LIBVIRT_DOMAIN_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_URL): cv.string,
        vol.Required(CONF_NAME): cv.string
    }
)


async def async_setup(hass, config):
    """Set up the libvirt component."""

    async def start_dom_libvirt(call):
        """Send magic packet to wake up a device."""
        url = call.data.get(CONF_URL)
        name = call.data.get(CONF_NAME)

        _LOGGER.info(
            ""
        )

        await hass.async_add_executor_job(
            partial(libvirt.start_dom_libvirt, url, name)
        )

    hass.services.async_register(
        DOMAIN,
        SERVICE_START_DOM_LIBVIRT,
        start_dom_libvirt,
        schema=LIBVIRT_DOMAIN_SCHEMA,
    )

    async def stop_dom_libvirt(call):
        """Send magic packet to wake up a device."""
        url = call.data.get(CONF_URL)
        name = call.data.get(CONF_NAME)

        _LOGGER.info(
            ""
        )

        await hass.async_add_executor_job(
            partial(libvirt.stop_dom_libvirt, url, name)
        )

    hass.services.async_register(
        DOMAIN,
        SERVICE_SHUTDOWN_DOM_LIBVIRT,
        stop_dom_libvirt,
        schema=LIBVIRT_DOMAIN_SCHEMA,
    )


    async def running_dom_libvirt(call):
        """Send magic packet to wake up a device."""
        url = call.data.get(CONF_URL)
        name = call.data.get(CONF_NAME)

        _LOGGER.info(
            ""
        )

        await hass.async_add_executor_job(
            partial(libvirt.running_dom_libvirt, url, name)
        )

    hass.services.async_register(
        DOMAIN,
        SERVICE_RUNNING_DOM_LIBVIRT,
        running_dom_libvirt,
        schema=LIBVIRT_DOMAIN_SCHEMA,
    )

    return True
