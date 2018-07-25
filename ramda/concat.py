from ramda.curry import curry


@curry
def concat(xs, ys):
    return xs + ys
