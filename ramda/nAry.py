import inspect
from ramda.curry import curry


def generate_args(spec, total):
    named = spec.args
    n_original = len(spec.args)
    add_args = ['None'] * (len(named) - total)
    named.extend([f'x{i}' for i in range(0, total - len(named))])
    return named, add_args, n_original


@curry
def nAry(n, f):
    if n < 0:
        raise ValueError(
            'First argument to nAry must be a non-negative integer'
        )

    args, add_args, n_original = generate_args(inspect.getfullargspec(f), n)

    args2 = args[0:min(n, n_original)] + add_args
    func = f'lambda {", ".join(args[0:n])}: f({", ".join(args2)})'
    return eval(func, {"f": f})
