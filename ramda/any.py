from ramda.curry import curry


@curry
def any(p, xs):
    for x in xs:
        if p(x) is True:
            return True
    return False
