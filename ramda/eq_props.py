from toolz import curry


@curry
def eq_props(prop, object1, object2):
    """Reports whether two objects have the same value, in R.equals
    terms, for the specified property. Useful as a curried predicate"""
    return object1[prop] == object2[prop]
