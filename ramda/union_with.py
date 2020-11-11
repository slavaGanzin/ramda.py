from toolz import curry
from ramda.none import none


@curry
def union_with(predicate, X, Y):
    """Combines two lists into a set (i.e. no duplicates) composed of the elements
    of each list. Duplication is determined according to the value returned by
    applying the supplied predicate to two list elements"""
    result = []
    for xy in X + Y:
        if none(predicate(xy), result):
            result.append(xy)
    return result
