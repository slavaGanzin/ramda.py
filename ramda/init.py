from builtins import list as _list


def init(list):
    """Returns all but the last element of the given list or string"""
    if isinstance(list, str):
        return list[:-1]

    return _list(list)[:-1]
