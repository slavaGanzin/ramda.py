from toolz import curry


@curry
def xprod(xs1, xs2):
    """Creates a new list out of the two supplied by creating each possible pair
    from the lists"""
    return [[x, y] for y in xs2 for x in xs1]
