from ramda.curry import curry


@curry
def drop_last_while(predicate, xs):
    for i, x in enumerate(reversed(xs)):
        if not predicate(x):
            return xs[:-i]
