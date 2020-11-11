from toolz import curry


@curry
def all(p, xs):
    """Returns true if all elements of the list match the predicate, false if
    there are any that don't.
    Dispatches to the all method of the second argument, if present.
    Acts as a transducer if a transformer is given in list position"""
    for x in xs:
        if not p(x):
            return False
    return True
