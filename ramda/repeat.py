from toolz import curry
from ramda import clone


def repeat(value, times):
    """Returns a fixed list of size n containing a specified identical value"""
    return [clone(value) for i in range(0, times)]
