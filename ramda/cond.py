from ramda.curry import curry


@curry
def cond(conditions, value):
    for predicate, transformer in conditions:
        if predicate(value):
            return transformer(value)
