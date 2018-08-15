from ramda.curry import curry


@curry
def inner_join(predicate, xs, ys):
    out = []
    for x in xs:
        for y in ys:
            if predicate(x, y):
                out.append(x)
    return out
