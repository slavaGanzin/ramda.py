from toolz import curry


@curry
def find_last(p, xs):
    """Returns the last element of the list which matches the predicate, or
    undefined if no element matches.
    Acts as a transducer if a transformer is given in list position"""
    for found in (x for x in reversed(xs) if p(x)):
        return found
