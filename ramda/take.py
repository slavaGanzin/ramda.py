from ramda.curry import curry
from builtins import list as _list


@curry
def take(n, list):
    """Returns the first n elements of the given list, string, or
transducer/transformer (or object with a take method).
Dispatches to the take method of the second argument, if present"""
    try:
        return list[:n]
    except TypeError:
        return _list(list)[:n]
