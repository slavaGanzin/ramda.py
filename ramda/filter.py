from ramda.curry import curry


@curry
def filter(p, xs):
    if not hasattr(xs, '__iter__'):
        return []

    return [x for x in xs if p(x)]
