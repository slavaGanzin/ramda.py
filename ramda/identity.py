from toolz import curry


@curry
def identity(x):
    """A function that does nothing but return the parameter supplied to it. Good
    as a default or placeholder function"""
    return x
