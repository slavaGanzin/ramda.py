def tail(xs):
    """Returns all but the first element of the given list or string (or object
with a tail method).
Dispatches to the slice method of the first argument, if present"""
    return xs[1:]
