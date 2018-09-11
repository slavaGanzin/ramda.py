from ramda.curry import curry
from ramda.equals import equals
from ramda.path import path as _path


@curry
def path_eq(path, equals_to, value):
    try:
        return equals(_path(path, value), equals_to)
    except KeyError:
        return False
