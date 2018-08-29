from ramda.curry import curry
from ramda.private.curry_spec.make_func_curry_spec\
    import CurrySpecVarargError


def partial(f, args):
    try:
        return curry(f)(*args)
    except CurrySpecVarargError:
        return f(*args)
