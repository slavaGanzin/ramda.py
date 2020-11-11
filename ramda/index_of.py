from toolz import curry
from ramda.equals import equals


@curry
def index_of(y, xs):
    """Returns the position of the first occurrence of an item in an array, or -1
    if the item is not included in the array. R.equals is used to
    determine equality"""
    eq_y = equals(y)
    for i, x in enumerate(xs):
        if eq_y(x):
            return i
    return -1
