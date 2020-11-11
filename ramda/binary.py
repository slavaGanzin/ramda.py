from .n_ary import n_ary


def binary(f):
    """Wraps a function of any arity (including nullary) in a function that accepts
    exactly 2 parameters. Any extraneous parameters will not be passed to the
    supplied function"""
    return n_ary(2, f)
