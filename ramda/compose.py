from functools import reduce


def compose(*funcs):
    """Performs right-to-left function composition. The rightmost function may have
    any arity; the remaining functions must be unary.
    Note: The result of compose is not automatically curried"""
    return lambda v: reduce(lambda accum, f: f(accum), funcs[::-1], v)
