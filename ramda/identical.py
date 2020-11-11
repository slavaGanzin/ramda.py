from toolz import curry


@curry
def identical(x, y):
    """Returns true if its arguments are identical, false otherwise. Values are
    identical if they reference the same memory. NaN is identical to NaN;
    0 and -0 are not identical"""
    return x is y
