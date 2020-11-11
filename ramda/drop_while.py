from toolz import curry


@curry
def drop_while(predicate, xs):
    """Returns a new list excluding the leading elements of a given list which
    satisfy the supplied predicate function. It passes each value to the supplied
    predicate function, skipping elements while the predicate function returns
    true. The predicate function is applied to one argument: (value).
    Dispatches to the dropWhile method of the second argument, if present.
    Acts as a transducer if a transformer is given in list position"""
    for i, x in enumerate(xs):
        if not predicate(x):
            return xs[i:]
