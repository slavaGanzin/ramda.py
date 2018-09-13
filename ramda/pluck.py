from ramda.curry import curry


@curry
def prop(key, x):
    try:
        return x[key]
    except KeyError:
        return None


@curry
def pluck(key, xs):
    """Returns a new list by plucking the same named property off all objects in
the list supplied.
pluck will work on
any functor in
addition to arrays, as it is equivalent to R.map(R.prop(k), f)"""
    return list(map(prop(key), xs))
