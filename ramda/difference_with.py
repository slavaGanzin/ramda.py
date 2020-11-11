from toolz import curry


@curry
def difference_with(f, xs, ys):
    """Finds the set (i.e. no duplicates) of all elements in the first list not
    contained in the second list. Duplication is determined according to the
    value returned by applying the supplied predicate to two list elements"""
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
