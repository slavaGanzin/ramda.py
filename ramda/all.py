from ramda.curry import curry


@curry
def all(p, xs):
    for x in xs:
        if p(x) is False:
            return False
    return True
