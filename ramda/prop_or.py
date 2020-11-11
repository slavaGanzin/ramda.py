from toolz import curry
from ramda.prop import prop
from ramda.default_to import default_to


@curry
def prop_or(default, property, object):
    """If the given, non-null object has an own property with the specified name,
    returns the value of that property. Otherwise returns the provided default
    value"""
    return default_to(default, prop(property, object))
