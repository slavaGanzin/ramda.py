import inspect
from toolz import curry


def generate_args(spec, n):
    args1 = spec.args
    n_original = len(spec.args)
    add_args = ["None"] * (len(args1) - n)
    args1.extend(["x" + str(i) for i in range(0, n - len(args1))])
    args2 = args1[0 : min(n, n_original)] + add_args
    return ", ".join(args1[0:n]), ", ".join(args2)


@curry
def n_ary(n, f):
    """Wraps a function of any arity (including nullary) in a function that accepts
exactly n parameters. Any extraneous parameters will not be passed to the
supplied function"""
    if n < 0:
        raise ValueError("First argument to n_ary must be a non-negative integer")

    args1, args2 = generate_args(inspect.getfullargspec(f), n)

    return eval("lambda " + args1 + ": f(" + args2 + ")", {"f": f})
