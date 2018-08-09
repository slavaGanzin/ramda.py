from ramda.curry import curry


@curry
def count_by(f, xs):
    acc = {}
    for x in xs:
        k = f(x)
        try:
            acc[k] += 1
        except KeyError:
            acc[k] = 1
    return acc
