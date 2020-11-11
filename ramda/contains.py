from toolz import curry


@curry
def contains(y, xs):
    """Returns true if the specified value is equal, in R.equals
    terms, to at least one element of the given list; false otherwise"""
    for x in xs:
        if y == x:
            return True
