from ramda.curry import curry


@curry
def if_else(predicate, on_true_func, on_false_func, value):
    return on_true_func(value) if predicate(value) else on_false_func(value)
