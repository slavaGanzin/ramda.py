from toolz import curry


@curry
def ap(fs, xs):
    """ap applies a list of functions to a list of values.
    Dispatches to the ap method of the second argument, if present. Also
    treats curried functions as applicatives"""
    acc = []
    for f in fs:
        for x in xs:
            acc.append(f(x))
    return acc
