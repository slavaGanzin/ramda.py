from toolz import curry


@curry
def prepend(value, list):
    """Returns a new list with the given element at the front, followed by the
    contents of the list"""
    return [value] + list
