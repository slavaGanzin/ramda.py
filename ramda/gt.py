from ramda.curry import curry


@curry
def gt(y, x):
    return x > y
