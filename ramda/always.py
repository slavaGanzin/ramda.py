from .curry import curry


@curry
def always(x, y):
    """Returns a function that always returns the given value. Note that for
    non-primitives the value returned is a reference to the original value.
    This function is known as const, constant, or K (for K combinator) in
    other languages and libraries"""
    return x
