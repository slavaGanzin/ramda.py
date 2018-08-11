from ramda.curry import curry
from ramda.clone import clone


@curry
def dissoc(key, object):
    o = clone(object)
    del o[key]
    return o
