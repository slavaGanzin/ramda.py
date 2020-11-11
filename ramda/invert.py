from toolz import curry


@curry
def invert(object):
    """Same as R.invertObj, however this accounts for objects with
    duplicate values by putting the values into an array"""
    if type(object) is dict:
        o = object.items()
    else:
        o = enumerate(object)

    out = {}
    for key, value in o:
        try:
            out[value].append(key)
        except KeyError:
            out[value] = [key]

    return out
