from ramda.curry import curry


@curry
def eq_by(predicate, a, b):
    return predicate(a) == predicate(b)
