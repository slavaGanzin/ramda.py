from toolz import curry
from builtins import range as _range


@curry
def range(from_, to):
    """Returns a list of numbers from from (inclusive) to to (exclusive)"""
    return list(_range(from_, to))
