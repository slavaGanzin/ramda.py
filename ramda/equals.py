from ramda.curry import curry


@curry
def equals(x, y):
    return x == y
