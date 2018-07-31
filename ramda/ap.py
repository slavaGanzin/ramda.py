from ramda.curry import curry


@curry
def ap(fs, xs):
    acc = []
    for f in fs:
        for x in xs:
            acc.append(f(x))
    return acc
