from ramda.curry import curry


@curry
def inc(x):
    return x + 1
