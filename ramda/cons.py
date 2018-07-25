from ramda.curry import curry


@curry
def cons(x, xs):
    return [x] + xs
