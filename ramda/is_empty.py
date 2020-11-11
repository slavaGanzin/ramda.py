def is_empty(xs):
    """Returns true if the given value is its type's empty value; false
    otherwise"""
    try:
        return len(xs) == 0
    except TypeError:
        return False
