from ramda.curry import curry


@curry
def drop(n, xs):
    return xs[n::]
