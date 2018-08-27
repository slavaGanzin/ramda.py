from ramda.curry import curry


@curry
def nth(n, xs):
    try:
        return xs[n]
    except IndexError:
        if type(xs) is str:
            return ''
        return None
