from ramda.curry import curry
from ramda.equals import equals
from .any_satisfy import any_satisfy


@curry
def contains(x, xs):
    return any_satisfy(equals(x), xs)
