from toolz import curry
from ramda.always import always
from ramda.reduce import reduce
from .both import both


@curry
def all_pass(ps, v):
    """Takes a list of predicates and returns a predicate that returns true for a
    given list of arguments if every one of the provided predicates is satisfied
    by those arguments.
    The function returned is a curried function whose arity matches that of the
    highest-arity predicate"""
    return reduce(both, always(True), ps)(v)
