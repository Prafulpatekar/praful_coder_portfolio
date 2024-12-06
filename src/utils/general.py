import yaml
import os
from typing import Dict, Any
from django.conf import settings
from django.db import transaction


def deep_update(base_dict: dict, update_with: dict) -> Dict[str, Dict]:
    """
    Method to replace dictionary values recursively, only updating keys present in the update_with dictionary.
    Args:
        base_dict (dict): The original dictionary to be updated.
        update_with (dict): The dictionary containing the updated values.

    Returns:
        dict: The updated base_dict.
    """
    for key, value in update_with.items():
        if isinstance(value, dict):
            base_dict_value = base_dict.get(key)

            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, value)
            else:
                base_dict[key] = value
        else:
            base_dict[key] = value

    return base_dict


def apply_on_commit(callable_):
    if settings.USE_ON_COMMIT_HOOK:
        transaction.on_commit(callable_)
    else:
        callable_()


def yaml_coerce(value):
    """
    This function is used to coerce a string value into its corresponding YAML data type.

    Args:
    - value (str): The string value to be coerced.

    Returns:
    - The coerced value of the input string. If the input is not a string, the function returns the input as is.

    Example:
    >>> yaml_coerce('123')
    123
    >>> yaml_coerce('true')
    True
    >>> yaml_coerce('null')
    None
    >>> yaml_coerce('[1, 2, 3]')
    [1, 2, 3]
    >>> yaml_coerce('{"key": "value"}')
    {'key': 'value'}
    >>> yaml_coerce('not a yaml string')
    'not a yaml string'
    """
    if isinstance(value, str):
        return yaml.load(f"dummy: {value}", Loader=yaml.SafeLoader)["dummy"]

    return value


def get_settings_from_environment(prefix: str) -> Dict[str, Any]:
    """
    This function retrieves environment variables starting with a given prefix,
    applies the yaml_coerce function to their values, and returns them as a dictionary.

    Parameters:
    - prefix (str): The prefix to match environment variable keys.

    Returns:
    - dict: A dictionary containing the coerced environment variables. The keys are the variable names without the prefix,
      and the values are the coerced variable values.

    Example:
        prefix = 'MYPORTFOLIO'
        env_var - 'MYPORTFOLIO_DB_USER="admin"'
        {
            'DB_USER': 'admin'
        }
    """
    prefix_len = len(prefix)
    return {
        key[prefix_len:]: yaml_coerce(value)
        for key, value in os.environ.items()
        if key.startswith(prefix)
    }
