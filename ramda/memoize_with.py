from toolz import curry


@curry
def memoize_with(key_generator, f):
    """A customisable version of R.memoize. memoizeWith takes an
    additional function that will be applied to a given argument set and used to
    create the cache key under which the results of the function to be memoized
    will be stored. Care must be taken when implementing key generation to avoid
    clashes that may overwrite previous entries erroneously"""

    def cache_closure():
        cache = {}

        def memoized(*args):
            k = key_generator(*args)
            if k not in cache:
                cache[k] = f(*args)

            return cache[k]
        return memoized

    return cache_closure()
