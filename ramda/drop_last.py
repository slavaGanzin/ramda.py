from toolz import curry


@curry
def drop_last(n, xs):
    """Returns a list containing all but the last n elements of the given list"""
    return xs[: -n or None]
