from toolz import curry
from ramda.clone import clone


@curry
def dissoc(key, object):
    """Returns a new object that does not contain a prop property"""
    o = clone(object)
    del o[key]
    return o
