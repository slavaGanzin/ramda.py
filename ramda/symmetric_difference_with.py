from toolz import curry
from ramda.difference_with import difference_with
from ramda.concat import concat


@curry
def symmetric_difference_with(predicate, first, second):
    """Finds the set (i.e. no duplicates) of all elements contained in the first or
    second list, but not both. Duplication is determined according to the value
    returned by applying the supplied predicate to two list elements"""
    return concat(
        difference_with(predicate, first, second),
        difference_with(predicate, second, first),
    )
