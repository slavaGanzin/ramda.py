import copy


def clone(v):
    """Creates a deep copy of the value which may contain (nested) Arrays and
    Objects, Numbers, Strings, Booleans and Dates. Functions are
    assigned by reference rather than copied
    Dispatches to a clone method if present"""
    return copy.deepcopy(v)
