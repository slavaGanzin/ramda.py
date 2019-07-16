from toolz import curry


@curry
def negate(x):
    """Negates its argument"""
    return -x
