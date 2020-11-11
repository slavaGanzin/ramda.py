import collections
from toolz import curry


@curry
def map_obj_indexed(f, xs):
    """An Object-specific version of map. The function is applied to three
    arguments: (value, key, obj). If only the value is significant, use
    map instead"""
    if isinstance(xs, collections.Mapping):
        obj = xs.items()
    else:
        obj = enumerate(xs)

    f_dict = {}

    for key, value in obj:
        f_dict[key] = f(value, key, obj)

    return f_dict
