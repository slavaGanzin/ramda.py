from toolz import curry


@curry
def lt(x, y):
    """Returns true if the first argument is less than the second; false
    otherwise"""
    return x < y
