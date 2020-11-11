import types
from toolz import curry


@curry
def bind(f, o):
    """Creates a function that is bound to a context.
    Note: R.bind does not provide the additional argument-binding capabilities of
    Function.prototype.bind"""
    return types.MethodType(f, o)
