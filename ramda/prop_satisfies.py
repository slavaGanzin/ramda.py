from toolz import curry
from ramda.prop import prop


@curry
def prop_satisfies(predicate, property, object):
    """Returns true if the specified object property satisfies the given
    predicate; false otherwise. You can test multiple properties with
    R.where"""
    return predicate(prop(property, object))
