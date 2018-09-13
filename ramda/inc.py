from ramda.curry import curry


@curry
def inc(x):
    """Increments its argument"""
    return x + 1
