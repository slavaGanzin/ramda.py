from toolz import curry


@curry
def find_index(p, xs):
    """Returns the index of the first element of the list which matches the
    predicate, or -1 if no element matches.
    Acts as a transducer if a transformer is given in list position"""
    for i in (i for i, x in enumerate(xs) if p(x)):
        return i
