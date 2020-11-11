from toolz import curry


@curry
def append(x, ys):
    """Returns a new list containing the contents of the given list, followed by
    the given element"""
    return list(ys) + [x]
