from toolz import curry


@curry
def both(p1, p2, v):
    """A function which calls the two provided functions and returns the &&
    of the results.
    It returns the result of the first function if it is false-y and the result
    of the second function otherwise. Note that this is short-circuited,
    meaning that the second function will not be invoked if the first returns a
    false-y value.
    In addition to functions, R.both also accepts any fantasy-land compatible
    applicative functor"""
    return p1(v) and p2(v)
