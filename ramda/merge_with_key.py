from toolz import curry
from ramda.clone import clone


@curry
def merge_with_key(function, object1, object2):
    """Creates a new object with the own properties of the two provided objects. If
    a key exists in both objects, the provided function is applied to the key
    and the values associated with the key in each object, with the result being
    used as the value associated with the key in the returned object"""

    out = clone(object1)
    for k, v in object2.items():
        out[k] = v if k not in out else function(k, out[k], v)
    return out
