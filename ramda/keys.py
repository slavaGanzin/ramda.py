from toolz import curry


@curry
def keys(dict):
    """Returns a list containing the names of all the enumerable own properties of
    the supplied object.
    Note that the order of the output array is not guaranteed to be consistent
    across different JS platforms"""
    return list(dict.keys())
