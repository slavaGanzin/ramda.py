from functools import reduce


def pipe(*funcs):
    """Performs left-to-right function composition. The leftmost function may have
    any arity; the remaining functions must be unary.
    In some libraries this function is named sequence.
    Note: The result of pipe is not automatically curried"""
    return lambda v: reduce(lambda accum, f: f(accum), funcs, v)
