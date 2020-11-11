from toolz import curry


@curry
def cond(conditions, value):
    """Returns a function, fn, which encapsulates if/else, if/else, ... logic.
    R.cond takes a list of [predicate, transformer] pairs. All of the arguments
    to fn are applied to each of the predicates in turn until one returns a
    "truthy" value, at which point fn returns the result of applying its
    arguments to the corresponding transformer. If none of the predicates
    matches, fn returns undefined"""
    for predicate, transformer in conditions:
        if predicate(value):
            return transformer(value)
