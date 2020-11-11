from toolz import curry


@curry
def drop(n, xs):
    """Returns all but the first n elements of the given list, string, or
    transducer/transformer (or object with a drop method).
    Dispatches to the drop method of the second argument, if present"""
    return xs[n::]
