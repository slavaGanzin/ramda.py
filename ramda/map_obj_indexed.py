import collections
from ramda.curry import curry


@curry
def map_obj_indexed(f, xs):
    """An Object-specific version of map. The function is applied to three
arguments: (value, key, obj). If only the value is significant, use
map instead"""
    if isinstance(xs, collections.Mapping):
        X = xs.items()
    else:
        X = enumerate(xs)

    f_dict = {}

    for k, v in X:
        f_dict[k] = f(v)
    return f_dict
