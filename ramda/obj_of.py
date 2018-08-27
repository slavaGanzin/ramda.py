from ramda.curry import curry


@curry
def obj_of(k, v):
    return {k: v}
