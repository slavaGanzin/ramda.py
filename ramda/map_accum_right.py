from toolz import curry


@curry
def map_accum_right(function, accumulator, list):
    """The mapAccumRight function behaves like a combination of map and reduce; it
    applies a function to each element of a list, passing an accumulating
    parameter from right to left, and returning a final value of this
    accumulator together with the new list.
    Similar to mapAccum, except moves through the input list from
    the right to the left.
    The iterator function receives two arguments, value and acc, and should
    return a tuple [value, acc]"""
    result = []
    for e in reversed(list):
        accumulator, r = function(e, accumulator)
        result.insert(0, r)
    return [result, accumulator]
