from toolz import curry


@curry
def drop_repeats_with(f, xs):
    """Returns a new list without any consecutively repeating elements. Equality is
    determined by applying the supplied predicate to each pair of consecutive elements. The
    first element in a series of equal elements will be preserved.
    Acts as a transducer if a transformer is given in list position"""
    out = [xs[0]]
    for i in range(0, len(xs) - 1):
        if not f(*xs[i : i + 2]):
            out.append(xs[i + 1])
    return out
