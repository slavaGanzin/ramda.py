from ramda.curry import curry


@curry
def converge(converging, branches, args):
    return converging(*[f(args) for f in branches])
