from toolz import curry
from ramda.private.curry_spec.make_func_curry_spec import CurrySpecVarargError


@curry
def partial(f, args):
    """Takes a function f and a list of arguments, and returns a function g.
    When applied, g returns the result of applying f to the arguments
    provided initially followed by the arguments provided to g"""
    try:
        return curry(f)(*args)
    except CurrySpecVarargError:
        return f(*args)
