import inspect
from ramda.curry import curry


# xs = lambda n: ', '.join([f'x{i}' for i in range(1, n+2)])
# '\n'.join([f'{n+1}: lambda {xs(n)}, *args:
# f({xs(n)}, *empty_args),' for n in range(-1, 10)])
@curry
def nAry(n, f):
    if n < 0 or n > 10:
        raise ValueError('\
First argument to nAry must be a non-negative integer no greater than ten')

    empty_args = [None] * (len(inspect.signature(f).parameters) - n)

    switch = {
        0: lambda: f(*empty_args),
        1: lambda x1:
            f(x1, *empty_args),
        2: lambda x1, x2:
            f(x1, x2, *empty_args),
        3: lambda x1, x2, x3:
            f(x1, x2, x3, *empty_args),
        4: lambda x1, x2, x3, x4:
            f(x1, x2, x3, x4, *empty_args),
        5: lambda x1, x2, x3, x4, x5:
            f(x1, x2, x3, x4, x5, *empty_args),
        6: lambda x1, x2, x3, x4, x5, x6:
            f(x1, x2, x3, x4, x5, x6, *empty_args),
        7: lambda x1, x2, x3, x4, x5, x6, x7:
            f(x1, x2, x3, x4, x5, x6, x7, *empty_args),
        8: lambda x1, x2, x3, x4, x5, x6, x7, x8:
            f(x1, x2, x3, x4, x5, x6, x7, x8, *empty_args),
        9: lambda x1, x2, x3, x4, x5, x6, x7, x8, x9:
            f(x1, x2, x3, x4, x5, x6, x7, x8, x9, *empty_args),
        10: lambda x1, x2, x3, x4, x5, x6, x7, x8, x9, x10:
            f(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, *empty_args),
    }

    return switch[n]
