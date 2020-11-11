from functools import wraps, partial
from ramda.private.curry_spec import (
    CurrySpec,
    ArgValues,
    make_func_curry_spec,
    remove_args_from_curry_spec,
    arg_values_fulfill_curry_spec,
)


def curry_by_spec(curry_spec, f):
    @wraps(f)
    def curried(*args, **kwargs):
        arg_values = ArgValues(args, kwargs)
        if arg_values_fulfill_curry_spec(curry_spec, arg_values):
            return f(*args, **kwargs)
        else:
            partialed_f = wraps(f)(partial(f, *args, **kwargs))
            new_spec = remove_args_from_curry_spec(curry_spec, arg_values)
            return curry_by_spec(new_spec, partialed_f)

    return curried


def curry(f):
    """Returns a curried equivalent of the provided function. The curried function
    has two unusual capabilities. First, its arguments needn't be provided one
    at a time. If f is a ternary function and g is R.curry(f), the
    following are equivalent:
    g(1)(2)(3)
    g(1)(2, 3)
    g(1, 2)(3)
    g(1, 2, 3)
    Secondly, the special placeholder value R.__ may be used to specify
    "gaps", allowing partial application of any combination of arguments,
    regardless of their positions. If g is as above and _ is R.__,
    the following are equivalent:
    g(1, 2, 3)
    g(_, 2, 3)(1)
    g(_, _, 3)(1)(2)
    g(_, _, 3)(1, 2)
    g(_, 2)(1)(3)
    g(_, 2)(1, 3)
    g(_, 2)(_, 3)(1)"""
    curry_spec = make_func_curry_spec(f)
    return curry_by_spec(curry_spec, f)
