from ramda.curry import curry
from ramda.equals import equals


@curry
def index_of(y, xs):
    eq_y = equals(y)
    for i, x in enumerate(xs):
        if eq_y(x):
            return i
    return -1
