from ramda.curry import curry


@curry
def reduce_while(predicate, iterator, accumulator, list):
    """Like reduce, reduceWhile returns a single item by iterating
through the list, successively calling the iterator function. reduceWhile
also takes a predicate that is evaluated before each step. If the predicate
returns false, it "short-circuits" the iteration and returns the current
value of the accumulator"""
    for x in list:
        if not predicate(accumulator, x):
            return accumulator
        accumulator = iterator(accumulator, x)
    return accumulator
