from toolz import curry
import builtins


@curry
def sum(xs):
    """Adds together all the elements of a list"""
    return builtins.sum(xs)
