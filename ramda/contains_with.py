from toolz import curry
from .any import any
from functools import partial


@curry
def contains_with(is_equal, x, xs):
    """Creates a new list out of the two supplied by applying the function to each
    equally-positioned pair in the lists. The returned list is truncated to the
    length of the shorter of the two input lists"""
    is_equal_to_x = partial(is_equal, x)
    return any(is_equal_to_x, xs)
