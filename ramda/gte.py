from toolz import curry


@curry
def gte(x, y):
    """Returns true if the first argument is greater than or equal to the second;
    false otherwise"""
    return x >= y
