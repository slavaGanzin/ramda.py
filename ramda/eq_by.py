from toolz import curry


@curry
def eq_by(predicate, a, b):
    """Takes a function and two values in its domain and returns true if the
    values map to the same value in the codomain; false otherwise"""
    return predicate(a) == predicate(b)
