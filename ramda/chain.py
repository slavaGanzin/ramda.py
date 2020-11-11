from toolz import curry
from .map import map
from .concat import concat
from .reduce import reduce


@curry
def chain(f, xs):
    """chain maps a function over a list and concatenates the results. chain
    is also known as flatMap in some libraries
    Dispatches to the chain method of the second argument, if present,
    according to the FantasyLand Chain spec"""
    return reduce(concat, [], map(f, xs))
