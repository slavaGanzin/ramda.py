from toolz import curry
from ramda.clone import clone


@curry
def assoc(key, value, object):
    """Makes a shallow clone of an object, setting or overriding the specified
    property with the given value. Note that this copies and flattens prototype
    properties onto the new object as well. All non-primitive properties are
    copied by reference"""
    o = clone(object)
    o[key] = value
    return o
