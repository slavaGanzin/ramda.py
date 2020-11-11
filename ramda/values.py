from toolz import curry


@curry
def values(dict):
    """Returns a list of all the enumerable own properties of the supplied object.
    Note that the order of the output array is not guaranteed across different
    JS platforms"""
    return list(dict.values())
