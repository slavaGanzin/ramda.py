from ramda.curry import curry


@curry
def find_index(p, xs):
    for i in (i for i, x in enumerate(xs) if p(x)):
        return i
