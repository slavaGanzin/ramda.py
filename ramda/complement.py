from ramda.curry import curry


@curry
def complement(p, v):
    """Takes a function f and returns a function g such that if called with the same arguments
when f returns a "truthy" value, g returns false and when f returns a "falsy" value g returns true.
R.complement may be applied to any functor"""
    return not p(v)
