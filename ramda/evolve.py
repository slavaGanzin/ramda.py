from toolz import curry
from ramda.clone import clone
from ramda.path import path
from ramda.assoc_path import assoc_path


@curry
def evolve(transformations, object):
    """Creates a new object by recursively evolving a shallow copy of object,
    according to the transformation functions. All non-primitive properties
    are copied by reference.
    A transformation function will not be invoked if its corresponding key
    does not exist in the evolved object"""
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
