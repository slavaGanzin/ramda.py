from toolz import curry


@curry
def any(p, xs):
    """Returns true if at least one of elements of the list match the predicate,
    false otherwise.
    Dispatches to the any method of the second argument, if present.
    Acts as a transducer if a transformer is given in list position"""
    for x in xs:
        if p(x):
            return True
    return False
