from ramda.n_ary import n_ary


def unary(function):
    """Wraps a function of any arity (including nullary) in a function that accepts
    exactly 1 parameter. Any extraneous parameters will not be passed to the
    supplied function"""
    return n_ary(1, function)
