from pyramda.function.curry import curry


@curry
def pluck(key, xs):
    return list(map(lambda x: x[key], xs))
