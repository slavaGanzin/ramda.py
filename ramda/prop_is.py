from ramda import prop, is_, curry


@curry
def prop_is(type, property, value):
    """Returns true if the specified object property is of the given type;
    false otherwise"""
    return is_(type, prop(property, value))
