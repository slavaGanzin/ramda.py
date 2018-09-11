from ramda.curry import curry
from ramda.path import path as _path


@curry
def path_satisfies(predicate, path, value):
    try:
        return predicate(_path(path, value))
    except KeyError:
        return False
