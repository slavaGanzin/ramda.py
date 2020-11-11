from toolz import curry


@curry
def zip_obj(key, val):
    """Creates a new object out of a list of keys and a list of values.
    Key/value pairing is truncated to the length of the shorter of the two lists.
    Note: zipObj is equivalent to pipe(zip, fromPairs)"""
    return dict(zip(key, val))
