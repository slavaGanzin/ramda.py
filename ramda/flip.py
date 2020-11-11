import inspect
from ramda.private.generate_args import generate_args
from .curry import curry, curry_by_spec
from ramda.private.curry_spec import make_func_curry_spec


@curry
def flip(f):
    """Returns a new function much like the supplied one, except that the first two
    arguments' order is reversed"""
    args = inspect.getfullargspec(f).args

    return eval(
        f"curry(lambda {','.join(flip_first_two(args))}: f({','.join(args)}))",
        {"f": f, "curry": curry},
    )


def flip_first_two(xs):
    return xs[1::-1] + xs[2::] if len(xs) > 1 else xs
