from toolz import curry
import builtins


@curry
def min(x, y):
    """Returns the smaller of its two arguments"""
    return builtins.min([x, y])
