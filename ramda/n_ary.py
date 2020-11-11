import inspect
from toolz import curry

from ramda.private.generate_args import generate_args


@curry
def n_ary(n, f):
    """Wraps a function of any arity (including nullary) in a function that accepts
    exactly n parameters. Any extraneous parameters will not be passed to the
    supplied function"""
    if n < 0:
        raise ValueError("First argument to n_ary must be a non-negative integer")

    args1, args2 = generate_args(inspect.getfullargspec(f).args, n)

    return eval("lambda " + args1 + ": f(" + args2 + ")", {"f": f})
