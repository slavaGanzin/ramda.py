import types
from ramda.curry import curry


@curry
def bind(f, o):
    return types.MethodType(f, o)
