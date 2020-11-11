from toolz import curry


@curry
def intersperse(separator, xs):
    """Creates a new list with the separator interposed between elements.
    Dispatches to the intersperse method of the second argument, if present"""
    if hasattr(xs, "intersperse"):
        return xs.intersperse(separator)
    out = [xs[0]]
    for x in xs[1:]:
        out += [separator, x]

    return out
