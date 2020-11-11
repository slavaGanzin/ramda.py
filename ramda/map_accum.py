from toolz import curry


@curry
def map_accum(function, accumulator, list):
    """The mapAccum function behaves like a combination of map and reduce; it
    applies a function to each element of a list, passing an accumulating
    parameter from left to right, and returning a final value of this
    accumulator together with the new list.
    The iterator function receives two arguments, acc and value, and should
    return a tuple [acc, value]"""
    result = []
    for e in list:
        accumulator, r = function(accumulator, e)
        result.append(r)
    return [accumulator, result]
