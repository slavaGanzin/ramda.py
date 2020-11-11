import collections
from toolz import curry


@curry
def for_each_obj_indexed(f, xs):
    """Iterate over an input object, calling a provided function fn for each
    key and value in the object.
    fn receives three argument: (value, key, obj)"""
    if isinstance(xs, collections.Mapping):
        X = xs.items()
    else:
        X = enumerate(xs)

    [f(v, k) for k, v in X]
