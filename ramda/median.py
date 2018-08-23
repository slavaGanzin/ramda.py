from ramda.curry import curry


@curry
def median(xs):
    _xs = sorted(xs)
    n = len(xs)
    i = n // 2
    if n < 1:
        return None

    if n % 2 == 0:
        return (_xs[i - 1] + _xs[i]) / 2.0

    return _xs[i]
