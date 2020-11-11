from toolz import curry


@curry
def drop_last_while(predicate, xs):
    """Returns a new list excluding all the tailing elements of a given list which
    satisfy the supplied predicate function. It passes each value from the right
    to the supplied predicate function, skipping elements until the predicate
    function returns a falsy value. The predicate function is applied to one argument:
    (value)"""
    for i, x in enumerate(reversed(xs)):
        if not predicate(x):
            return xs[:-i]
