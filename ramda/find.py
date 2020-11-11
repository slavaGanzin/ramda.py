from toolz import curry


@curry
def find(p, xs):
    """Returns the first element of the list which matches the predicate, or
    undefined if no element matches.
    Dispatches to the find method of the second argument, if present.
    Acts as a transducer if a transformer is given in list position"""
    for found in (x for x in xs if p(x)):
        return found
