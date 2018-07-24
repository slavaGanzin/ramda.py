from ramda.function.curry import curry


@curry
def concat(xs, ys):
    return xs + ys
