from toolz import curry
from ramda.equals import equals
from ramda.path import path as _path


@curry
def path_eq(path, equals_to, value):
    """Determines whether a nested path on an object has a specific value, in
    R.equals terms. Most likely used to filter a list"""
    return equals(_path(path, value), equals_to)
