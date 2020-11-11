from toolz import curry


@curry
def uniq_by(predicate, list):
    """Returns a new list containing only one copy of each element in the original
    list, based upon the value returned by applying the supplied function to
    each list element. Prefers the first item if the supplied function produces
    the same value on two items. R.equals is used for comparison"""
    used = set()
    return [x for x in list if predicate(x) not in used and not used.add(predicate(x))]
