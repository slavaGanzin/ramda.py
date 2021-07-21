from toolz import curry
from ramda.default_to import default_to
from ramda.path import path as _path


@curry
def path_or(default, path, value):
    """If the given, non-null object has a value at the given path, returns the
    value at that path. Otherwise returns the provided default value"""
    return default_to(default, _path(path, value))
