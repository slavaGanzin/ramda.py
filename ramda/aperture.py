from toolz import curry


@curry
def aperture(n, xs):
    """Returns a new list, composed of n-tuples of consecutive elements. If n is
    greater than the length of the list, an empty list is returned.
    Acts as a transducer if a transformer is given in list position"""
    return [list(xs)[i : i + n] for i in range(0, int(len(xs) / n) * n)]
