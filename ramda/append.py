from ramda.curry import curry


@curry
def append(x, ys):
    """Returns a new list containing the contents of the given list, followed by
the given element"""
    ys.append(x)
    return ys
