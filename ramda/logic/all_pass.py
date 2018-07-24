from ramda.function.curry import curry
from ramda.function.always import always
from ramda.iterable.reduce import reduce
from .both import both


@curry
def all_pass(ps, v):
    return reduce(both, always(True), ps)(v)
