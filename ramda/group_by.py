from ramda.curry import curry


@curry
def group_by(f, xs):
    acc = {}
    for x in xs:
        key = f(x)
        try:
            acc[key].append(x)
        except KeyError:
            acc[key] = [x]

    return acc
