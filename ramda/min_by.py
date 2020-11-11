from toolz import curry


@curry
def min_by(f, x, y):
    """Takes a function and two values, and returns whichever value produces the
    smaller result when passed to the provided function"""
    return x if f(x) < f(y) else y
