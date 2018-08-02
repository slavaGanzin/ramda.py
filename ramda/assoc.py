from ramda.curry import curry
from ramda.clone import clone


@curry
def assoc(k, v, o):
    o = clone(o)
    o[k] = v
    return o
