from ramda.curry import curry


@curry
def from_pairs(pairs):
    out = {}
    for (k, v) in pairs:
        out[k] = v

    return out
