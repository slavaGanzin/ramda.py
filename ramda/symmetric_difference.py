from toolz import curry
from ramda.difference import difference
from ramda.concat import concat


@curry
def symmetric_difference(first, second):
    """Finds the set (i.e. no duplicates) of all elements contained in the first or
    second list, but not both"""
    return concat(difference(first, second), difference(second, first))
