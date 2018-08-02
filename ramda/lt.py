from ramda.curry import curry


@curry
def lt(y, x):
    return x < y
