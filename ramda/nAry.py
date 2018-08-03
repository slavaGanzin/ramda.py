import inspect
from ramda.curry import curry


def generate_args(spec, n):
    args1 = spec.args
    n_original = len(spec.args)
    add_args = ['None'] * (len(args1) - n)
    args1.extend([f'x{i}' for i in range(0, n - len(args1))])
    args2 = args1[0:min(n, n_original)] + add_args
    return args1[0:n], args2


@curry
def nAry(n, f):
    if n < 0:
        raise ValueError(
            'First argument to nAry must be a non-negative integer'
        )

    args1, args2 = generate_args(inspect.getfullargspec(f), n)

    func = f'lambda {", ".join(args1)}: f({", ".join(args2)})'
    return eval(func, {"f": f})
