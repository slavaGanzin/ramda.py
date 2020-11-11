from toolz import curry


def call(f, *args):
    """Returns the result of calling its first argument with the remaining
    arguments. This is occasionally useful as a converging function for
    R.converge: the first branch can produce a function while the
    remaining branches produce values to be passed to that function as its
    arguments"""
    if len(args) > 1:
        return f(*args)

    return lambda *args: f(*args)
