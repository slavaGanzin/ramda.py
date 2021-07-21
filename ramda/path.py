from toolz import curry
from ramda.prop import prop


@curry
def path(keys, dict):
    """Retrieve the value at a given path"""
    if not keys:
        raise ValueError("Expected at least one key, got {0}".format(keys))
    current_value = dict
    for key in keys:
        current_value = prop(key, current_value)
    return current_value
