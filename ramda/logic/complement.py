from ramda.function.curry import curry


@curry
def complement(p, v):
    return not p(v)
