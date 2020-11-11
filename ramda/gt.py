from toolz import curry


@curry
def gt(y, x):
    """Returns true if the first argument is greater than the second; false
    otherwise"""
    return x > y
