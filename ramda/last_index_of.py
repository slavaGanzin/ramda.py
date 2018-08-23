from ramda.curry import curry
from ramda.equals import equals


@curry
def last_index_of(y, xs):
    eq_y = equals(y)
    for i, x in enumerate(reversed(xs)):
        if eq_y(x):
            return len(xs) - i - 1
    return -1
