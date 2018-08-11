from ramda.curry import curry


@curry
def find_last(p, xs):
    for found in (x for x in reversed(xs) if p(x)):
        return found
