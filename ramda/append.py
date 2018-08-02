from ramda.curry import curry


@curry
def append(x, ys):
    ys.append(x)
    return ys
