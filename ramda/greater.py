from toolz import curry


@curry
def greater(a, b):
    """Creates a new list out of the two supplied by applying the function to each
    equally-positioned pair in the lists. The returned list is truncated to the
    length of the shorter of the two input lists"""
    return a if a >= b else b
