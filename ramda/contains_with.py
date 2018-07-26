from ramda.curry import curry
from .any import any
from functools import partial


@curry
def contains_with(is_equal, x, xs):
    is_equal_to_x = partial(is_equal, x)
    return any(is_equal_to_x, xs)
