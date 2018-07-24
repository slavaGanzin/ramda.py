from ramda.function.curry import curry


@curry
def inc(x):
    return x + 1
