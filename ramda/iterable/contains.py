from ramda.function.curry import curry
from ramda.relation.equals import equals
from .any_satisfy import any_satisfy


@curry
def contains(x, xs):
    return any_satisfy(equals(x), xs)
