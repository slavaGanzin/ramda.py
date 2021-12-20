from toolz import curry


@curry
def gt(x, y):
    """Returns true if the first argument is greater than the second; false
    otherwise"""
    return x > y
