from ramda.curry import curry


@curry
def drop_while(predicate, xs):
    for i, x in enumerate(xs):
        if not predicate(x):
            return xs[i:]
