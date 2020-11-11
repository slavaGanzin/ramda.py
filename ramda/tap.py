from toolz import curry


@curry
def tap(f, v):
    """Runs the given function with the supplied object, then returns the object.
    Acts as a transducer if a transformer is given as second parameter"""
    f(v)
    return v
