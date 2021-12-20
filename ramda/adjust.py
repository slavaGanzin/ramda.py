from toolz import curry
from .clone import clone


@curry
def adjust(i, f, xs):
    """Applies a function to the value at the given index of an array, returning a
    new copy of the array with the element at the given index replaced with the
    result of the function application"""
    _xs = clone(xs)
    _xs[i] = f(_xs[i])
    return _xs
