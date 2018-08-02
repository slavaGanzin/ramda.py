from ramda.curry import curry


@curry
def map(f, xs):
    return [f(x) for x in xs]
