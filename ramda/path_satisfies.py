from toolz import curry
from ramda.path import path as _path


@curry
def path_satisfies(predicate, path, value):
    """Returns true if the specified object property at given path satisfies the
    given predicate; false otherwise"""
    try:
        return predicate(_path(path, value))
    except KeyError:
        return False
