from toolz import curry


@curry
def default_to(default, x):
    """Returns the second argument if it is not null, undefined or NaN;
    otherwise the first argument is returned"""
    return default if x is None else x
