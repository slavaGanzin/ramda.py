from toolz import curry


@curry
def zip_with(f, xs1, xs2):
    """Creates a new list out of the two supplied by applying the function to each
    equally-positioned pair in the lists. The returned list is truncated to the
    length of the shorter of the two input lists"""
    return [f(x, y) for x, y in zip(xs1, xs2)]
