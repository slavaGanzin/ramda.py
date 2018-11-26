from ramda.curry import curry
import builtins


@curry
def is_(type, v):
    return builtins.isinstance(v, type)
