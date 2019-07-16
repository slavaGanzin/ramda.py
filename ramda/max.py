from toolz import curry
import builtins


@curry
def max(x, y):
    """Returns the larger of its two arguments"""
    return builtins.max([x, y])
