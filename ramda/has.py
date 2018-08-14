from ramda.curry import curry


@curry
def has(name, o):
    try:
        o[name]
        return True
    except KeyError:
        try:
            return hasattr(o, name)
        except AttributeError:
            return False
