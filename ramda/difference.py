from ramda.curry import curry


@curry
def difference(xs, ys):
    out = []
    for x in xs:
        if x not in ys:
            out.append(x)

    return out
