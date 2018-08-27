from ramda.curry import curry


@curry
def none(p, xs):
    for x in xs:
        if p(x):
            return False
    return True
