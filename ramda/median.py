from toolz import curry


@curry
def median(xs):
    """Returns the median of the given list of numbers"""
    _xs = sorted(xs)
    n = len(xs)
    i = n // 2
    if n < 1:
        return None

    if n % 2 == 0:
        return (_xs[i - 1] + _xs[i]) / 2.0

    return _xs[i]
