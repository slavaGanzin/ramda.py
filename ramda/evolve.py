from ramda.curry import curry
from ramda.clone import clone
from ramda.path import path
from ramda.assoc_path import assoc_path


@curry
def evolve(transformations, object):
    o = clone(object)
    for k, v in transformations.items():
        try:
            if isinstance(v, dict):
                o[k] = evolve(v, o[k])
            else:
                o[k] = v(o[k])
        except KeyError:
            continue

    return o
