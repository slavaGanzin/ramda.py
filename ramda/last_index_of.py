from toolz import curry
from ramda.equals import equals


@curry
def last_index_of(y, xs):
    """Returns the position of the last occurrence of an item in an array, or -1 if
    the item is not included in the array. R.equals is used to
    determine equality"""
    eq_y = equals(y)
    for i, x in enumerate(reversed(xs)):
        if eq_y(x):
            return len(xs) - i - 1
    return -1
