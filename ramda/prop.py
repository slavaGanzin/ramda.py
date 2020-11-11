from toolz import curry
import builtins


@curry
def prop(name, o):
    """Returns a function that when supplied an object returns the indicated
    property of that object, if it exists"""
    try:
        return builtins.getattr(o, name)
    except (AttributeError, TypeError):
        try:
            return o[name]
        except KeyError:
            return None
