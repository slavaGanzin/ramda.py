from ramda.curry import curry


@curry
def index_by(f, xs):
    out = {}
    for x in xs:
        out[f(x)] = x

    return out
