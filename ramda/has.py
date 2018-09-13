from ramda.curry import curry


@curry
def has(name, o):
    """Returns whether or not an object has an own property with the specified name"""
    try:
        o[name]
        return True
    except KeyError:
        try:
            return hasattr(o, name)
        except AttributeError:
            return False
