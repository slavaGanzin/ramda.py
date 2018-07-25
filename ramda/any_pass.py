from ramda.curry import curry
from ramda.always import always
from ramda.reduce import reduce
from .either import either


@curry
def any_pass(ps, v):
    return reduce(either, always(False), ps)(v)
