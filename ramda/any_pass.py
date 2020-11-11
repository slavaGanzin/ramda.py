from toolz import curry
from ramda.always import always
from ramda.reduce import reduce
from .either import either


@curry
def any_pass(ps, v):
    """Takes a list of predicates and returns a predicate that returns true for a
    given list of arguments if at least one of the provided predicates is
    satisfied by those arguments.
    The function returned is a curried function whose arity matches that of the
    highest-arity predicate"""
    return reduce(either, always(False), ps)(v)
