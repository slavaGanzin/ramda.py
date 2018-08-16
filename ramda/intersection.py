from ramda.curry import curry


@curry
def intersection(xs, ys):
    out = []
    for y in ys:
        for x in xs:
            if x == y and x not in out:
                out.append(x)
    return out
