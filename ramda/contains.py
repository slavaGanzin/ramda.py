from ramda.curry import curry
from ramda.equals import equals
from .any import any


@curry
def contains(x, xs):
    return any(equals(x), xs)
