from toolz import curry
from ramda.prop import prop
from ramda.equals import equals


@curry
def eq_props(property, object1, object2):
    """Reports whether two objects have the same value, in R.equals
    terms, for the specified property. Useful as a curried predicate"""
    return equals(prop(property, object1), prop(property, object2))
