from collections import Iterable
from past.builtins import basestring

from ramda.isinstance import isinstance
from ramda.curry import curry


@curry
def flatten_until(is_leaf, xs):
    """Returns a new list by pulling every item out of it (and all its sub-arrays)
and putting them in a new array, depth-first"""

    def _flatten_until(items):
        if isinstance(Iterable, items) and not is_leaf(items):
            for item in items:
                for i in _flatten_until(item):
                    yield i
        else:
            yield items

    return list(_flatten_until(xs))


flatten = flatten_until(isinstance(basestring))
