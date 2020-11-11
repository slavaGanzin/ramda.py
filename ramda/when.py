from toolz import curry


@curry
def when(predicate, when_true_fn, value):
    """Tests the final argument by passing it to the given predicate function. If
    the predicate is satisfied, the function will return the result of calling
    the whenTrueFn function with the same argument. If the predicate is not
    satisfied, the argument is returned as is"""
    if predicate(value):
        return when_true_fn(value)

    return value
