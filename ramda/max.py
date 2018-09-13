from ramda.curry import curry
import builtins


@curry
def max(xs):
    """Returns the larger of its two arguments"""
    return builtins.max(xs)
