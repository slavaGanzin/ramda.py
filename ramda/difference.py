from ramda.curry import curry


@curry
def difference(xs, ys):
    out = []
    for x in xs:
        if x not in ys and x not in out:
            out.append(x)

    return out
