from toolz import curry
from ramda.prop import prop


@curry
def props(properties, object):
    """Acts as multiple prop: array of keys in, array of values out. Preserves
    order"""
    return [prop(p, object) for p in properties]
