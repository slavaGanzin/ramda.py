from toolz import curry


@curry
def nth(n, xs):
    """Returns the nth element of the given list or string. If n is negative the
    element at index length + n is returned"""
    try:
        return xs[n]
    except IndexError:
        if type(xs) is str:
            return ""
        return None
