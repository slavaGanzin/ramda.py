from toolz import curry
from ramda.equals import equals


@curry
def prop_eq(property, value, object):
    """Returns true if the specified object property is equal, in
    R.equals terms, to the given value; false otherwise.
    You can test multiple properties with R.where"""
    try:
        return equals(object[property], value)
    except KeyError:
        return False
