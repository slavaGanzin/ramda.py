from ramda.curry import curry
from ramda.always import always
from ramda.reduce import reduce
from .both import both


@curry
def all_pass(ps, v):
    return reduce(both, always(True), ps)(v)
