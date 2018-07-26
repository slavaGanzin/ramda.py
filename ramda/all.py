from ramda.curry import curry

_all = all


@curry
def all(p, xs):
    return _all(map(p, xs))
