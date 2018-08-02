from ramda.curry import curry


@curry
def gte(y, x):
    return x >= y
