from toolz import curry


@curry
def from_pairs(pairs):
    """Creates a new object from a list key-value pairs. If a key appears in
    multiple pairs, the rightmost pair is included in the object"""
    out = {}
    for (k, v) in pairs:
        out[k] = v

    return out
