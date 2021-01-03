from ramda.curry import curry


@curry
def has(name, o):
    """Returns whether or not an object has an own property with the specified name"""
    if hasattr(o, str(name)):
        return True

    try:
        o[name]
        return True
    except (TypeError, KeyError):
        return False
