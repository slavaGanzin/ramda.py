from ramda.curry import curry


@curry
def negate(x):
    """Negates its argument"""
    return -x
