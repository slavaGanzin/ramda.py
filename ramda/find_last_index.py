from toolz import curry


@curry
def find_last_index(p, xs):
    """Returns the index of the last element of the list which matches the
    predicate, or -1 if no element matches.
    Acts as a transducer if a transformer is given in list position"""
    for i in (i for i, x in enumerate(reversed(xs)) if p(x)):
        return len(xs) - i
