from toolz import curry
from builtins import list as _list


@curry
def take_last(n, list):
    """Returns a new list containing the last n elements of the given list.
If n > list.length, returns a list of list.length elements"""
    if len(list) <= n:
        return list

    if isinstance(list, str):
        return list[-n:]

    acc = []

    i = 0
    for e in reversed(list):
        i += 1
        if i > n:
            return acc
        acc.insert(0, e)
