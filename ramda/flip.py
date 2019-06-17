from .curry import curry, curry_by_spec

from ramda.private.curry_spec import make_func_curry_spec


@curry
def flip(f):
    """Returns a new function much like the supplied one, except that the first two
arguments' order is reversed"""

    def wrapped(*args, **kwargs):
        return f(*flip_first_two(args), **kwargs)

    f_spec = make_func_curry_spec(f)

    return curry_by_spec(f_spec, wrapped)


def flip_first_two(xs):
    return xs[1::-1] + xs[2::] if len(xs) > 1 else xs
