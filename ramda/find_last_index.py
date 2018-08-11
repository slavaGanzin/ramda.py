from ramda.curry import curry


@curry
def find_last_index(p, xs):
    for i in (i for i, x in enumerate(reversed(xs)) if p(x)):
        return len(xs) - i
