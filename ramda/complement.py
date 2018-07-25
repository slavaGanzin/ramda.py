from ramda.curry import curry


@curry
def complement(p, v):
    return not p(v)
