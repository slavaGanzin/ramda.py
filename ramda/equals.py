from toolz import curry


@curry
def equals(x, y):
    """Returns true if its arguments are equivalent, false otherwise. Handles
    cyclical data structures.
    Dispatches symmetrically to the equals methods of both arguments, if
    present"""
    return x == y
