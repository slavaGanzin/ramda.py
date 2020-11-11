from toolz import curry
from ramda.clone import clone


@curry
def assoc_path(path, value, object):
    """Makes a shallow clone of an object, setting or overriding the nodes required
    to create the given path, and placing the specific value at the tail end of
    that path. Note that this copies and flattens prototype properties onto the
    new object as well. All non-primitive properties are copied by reference"""
    o = _o = clone(object)
    for k in path[:-1]:
        if not (k in _o and isinstance(_o[k], dict)):
            _o[k] = {}
        _o = _o[k]

    _o[path[-1]] = value
    return o
