from toolz import curry


@curry
def lte(x, y):
    """Returns true if the first argument is less than or equal to the second;
    false otherwise"""
    return x <= y
