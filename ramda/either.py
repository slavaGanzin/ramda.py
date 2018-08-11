from ramda.curry import curry


@curry
def either(predicate1, predicate2, value):
    return predicate1(value) or predicate2(value)
