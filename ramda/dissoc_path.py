from ramda.curry import curry
from ramda.clone import clone


@curry
def dissoc_path(path, object):
    _o = o = clone(object)
    for k in path[:-1]:
        _o = _o[k]

    del _o[path[-1]]

    return o
