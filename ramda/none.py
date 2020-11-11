from toolz import curry


@curry
def none(predicate, X):
    """Returns true if no elements of the list match the predicate, false
    otherwise.
    Dispatches to the any method of the second argument, if present"""
    for x in X:
        if predicate(x):
            return False
    return True
