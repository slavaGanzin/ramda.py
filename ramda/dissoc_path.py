from toolz import curry
from ramda.clone import clone


@curry
def dissoc_path(path, object):
    """Makes a shallow clone of an object, omitting the property at the given path.
    Note that this copies and flattens prototype properties onto the new object
    as well. All non-primitive properties are copied by reference"""
    _o = o = clone(object)
    for k in path[:-1]:
        _o = _o[k]

    del _o[path[-1]]

    return o
