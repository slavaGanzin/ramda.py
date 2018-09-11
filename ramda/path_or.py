from ramda.curry import curry
from ramda.default_to import default_to
from ramda.path import path as _path


@curry
def path_or(default, path, value):
    try:
        return default_to(default, _path(path, value))
    except KeyError:
        return default
