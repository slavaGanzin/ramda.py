from builtins import reversed
from builtins import list as _list


def reverse(list):
    """Returns a new list or string with the elements or characters in reverse
    order"""
    if isinstance(list, str):
        return "".join(reversed(list))

    return _list(reversed(list))
