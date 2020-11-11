from toolz import curry


@curry
def if_else(predicate, on_true_func, on_false_func, value):
    """Creates a function that will process either the onTrue or the onFalse
    function depending upon the result of the condition predicate"""
    return on_true_func(value) if predicate(value) else on_false_func(value)
