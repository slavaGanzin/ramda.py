from ramda.curry import curry
import builtins


@curry
def min(xs):
    """Returns the smaller of its two arguments"""
    return builtins.min(xs)
