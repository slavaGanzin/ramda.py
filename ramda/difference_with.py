from ramda.curry import curry


@curry
def difference_with(f, xs, ys):
    out = []
    for x in xs:
        if x in out:
            continue

        contains = False
        for y in ys:
            if f(x, y):
                contains = True
                break

        if not contains:
            out.append(x)

    return out
