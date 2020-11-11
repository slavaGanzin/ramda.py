from toolz import curry


@curry
def until(predicate, transformation, value):
    """Takes a predicate, a transformation function, and an initial value,
    and returns a value of the same type as the initial value.
    It does so by applying the transformation until the predicate is satisfied,
    at which point it returns the satisfactory value"""
    out = transformation(value)
    while predicate(out):
        out = transformation(out)
    return out
