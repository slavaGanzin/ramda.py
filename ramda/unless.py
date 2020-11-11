from toolz import curry


@curry
def unless(predicate, function, value):
    """Tests the final argument by passing it to the given predicate function. If
    the predicate is not satisfied, the function will return the result of
    calling the whenFalseFn function with the same argument. If the predicate
    is satisfied, the argument is returned as is"""
    if predicate(value):
        return value
    return function(value)
