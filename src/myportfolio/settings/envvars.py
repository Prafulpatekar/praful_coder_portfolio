"""
This takes env variables with matching prefix, strips out the prefix, and adds it to global settings.

For example:
    export PORTFOLIO_SETTINGS_IN_DOCKER=true (environment variable)
    could then be reffered as a global as:
    IN_DOCKER (where then value would be True)
"""
from src.utils.general import deep_update, get_settings_from_environment

from . import ENVVAR_SETTINGS_PREFIX

# global() is a dictionary of global variables
deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821
