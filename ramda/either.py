from toolz import curry


@curry
def either(predicate1, predicate2, value):
    """A function wrapping calls to the two functions in an || operation,
    returning the result of the first function if it is truth-y and the result
    of the second function otherwise. Note that this is short-circuited,
    meaning that the second function will not be invoked if the first returns a
    truth-y value.
    In addition to functions, R.either also accepts any fantasy-land compatible
    applicative functor"""
    return predicate1(value) or predicate2(value)
