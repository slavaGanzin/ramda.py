from ramda.curry import curry


@curry
def none(p, xs):
    """Returns true if no elements of the list match the predicate, false
otherwise.
Dispatches to the any method of the second argument, if present"""
    for x in xs:
        if p(x):
            return False
    return True
