from toolz import curry


@curry
def invert_obj(object):
    """Returns a new object with the keys of the given object as values, and the
    values of the given object, which are coerced to strings, as keys. Note
    that the last key found is preferred when handling the same value"""
    if hasattr(object, "items"):
        o = object.items()
    else:
        o = enumerate(object)

    out = {}
    for key, value in o:
        if hasattr(value, "__iter__") and type(value) != str:
            for v in value:
                out[v] = key
        else:
            out[value] = key
    return out


invert_obj(["alice", "jave"])
