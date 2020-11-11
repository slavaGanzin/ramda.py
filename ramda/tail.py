from builtins import list as _list


def tail(list):
    """Returns all but the first element of the given list or string (or object
    with a tail method).
    Dispatches to the slice method of the first argument, if present"""
    if isinstance(list, str):
        return list[1:]

    return _list(list)[1:]
