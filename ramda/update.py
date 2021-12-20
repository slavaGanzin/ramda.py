from toolz import curry
from .clone import clone


@curry
def update(i, v, xs):
    """Returns a new copy of the array with the element at the provided index
    replaced with the given value"""
    _xs = clone(xs)
    _xs[i] = v
    return _xs
