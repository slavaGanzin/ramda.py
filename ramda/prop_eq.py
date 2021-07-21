from toolz import curry
from ramda.equals import equals
from ramda.prop import prop


@curry
def prop_eq(property, value, object):
    """Returns true if the specified object property is equal, in
    R.equals terms, to the given value; false otherwise.
    You can test multiple properties with R.where"""
    return equals(prop(property, object), value)
