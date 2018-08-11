from ramda.curry import curry
from ramda.clone import clone


@curry
def assoc(key, value, object):
    o = clone(object)
    o[key] = value
    return o
