from toolz import curry


@curry
def obj_of(k, v):
    """Creates an object containing a single key:value pair"""
    return {k: v}
