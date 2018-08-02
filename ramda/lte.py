from ramda.curry import curry


@curry
def lte(y, x):
    return x <= y
