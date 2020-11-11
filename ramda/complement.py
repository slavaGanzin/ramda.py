import inspect
from toolz import compose


def complement(f):
    """Takes a function f and returns a function g such that if called with the same arguments
    when f returns a "truthy" value, g returns false and when f returns a "falsy" value g returns true.
    R.complement may be applied to any functor"""
    return compose(lambda *x: not x[0], f)
