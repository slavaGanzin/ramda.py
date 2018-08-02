from ramda.curry import curry


@curry
def assoc(k, v, o):
    o[k] = v
    return o
