from ramda.curry import curry
from ramda.clone import clone


@curry
def assoc_path(ks, v, o):
    o = _o = clone(o)
    for k in ks[:-1]:
        if not (k in _o and isinstance(_o[k], dict)):
            _o[k] = {}
        _o = _o[k]

    _o[ks[-1]] = v
    return o
