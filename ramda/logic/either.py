from ramda.function.curry import curry


@curry
def either(p1, p2, v):
    return p1(v) or p2(v)
