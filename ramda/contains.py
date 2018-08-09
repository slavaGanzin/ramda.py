from ramda.curry import curry


@curry
def contains(y, xs):
    for x in xs:
        if y == x:
            return True
