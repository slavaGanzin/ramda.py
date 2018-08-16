from ramda.curry import curry


@curry
def intersperse(separator, xs):
    if hasattr(xs, 'intersperse'):
        return xs.intersperse(separator)
    out = [xs[0]]
    for x in xs[1:]:
        out += [separator, x]

    return out
