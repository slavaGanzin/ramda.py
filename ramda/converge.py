from toolz import curry


@curry
def converge(converging, branches, args):
    """Accepts a converging function and a list of branching functions and returns
    a new function. When invoked, this new function is applied to some
    arguments, each branching function is applied to those same arguments. The
    results of each branching function are passed as arguments to the converging
    function to produce the return value"""
    return converging(*[f(args) for f in branches])
