from ramda.function.curry import curry
from ramda.function.always import always
from ramda.iterable.reduce import reduce
from .either import either


@curry
def any_pass(ps, v):
    return reduce(either, always(False), ps)(v)
