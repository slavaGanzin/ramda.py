from toolz import curry


@curry
def split(separator, string):
    """Splits a string into an array of strings based on the given
    separator"""
    return string.split(separator)
