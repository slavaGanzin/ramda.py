from ramda.curry import curry
from ramda.equals import equals


@curry
def prop_eq(property, value, object):
    try:
        return equals(object[property], value)
    except KeyError:
        return False
