from ramda.curry import curry


@curry
def memoize_with(key_generator, f):
    cache = {}

    def memoized(*args):
        k = key_generator(*args)
        try:
            return cache[k]
        except KeyError:
            cache[k] = f(*args)
            return cache[k]

    return memoized
