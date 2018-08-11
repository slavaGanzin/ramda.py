from ramda.curry import curry
from ramda.clone import clone


@curry
def assoc_path(path, value, object):
    o = _o = clone(object)
    for k in path[:-1]:
        if not (k in _o and isinstance(_o[k], dict)):
            _o[k] = {}
        _o = _o[k]

    _o[path[-1]] = value
    return o
