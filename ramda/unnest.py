import collections
from ramda.identity import identity
from ramda.chain import chain


def unnest(list):
    """Shorthand for R.chain(R.identity), which removes one level of nesting from
    any Chain"""
    out = []
    for e in list:
        if isinstance(e, collections.Sequence):
            out += e
        else:
            out.append(e)
    return out
