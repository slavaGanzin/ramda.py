from ramda.curry import curry


@curry
def take(n, xs):
    return xs[:n]
