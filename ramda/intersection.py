from toolz import curry


@curry
def intersection(xs, ys):
    """Combines two lists into a set (i.e. no duplicates) composed of those
elements common to both lists"""
    out = []
    for y in ys:
        for x in xs:
            if x == y and x not in out:
                out.append(x)
    return out
