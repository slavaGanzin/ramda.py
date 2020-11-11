from ramda import curry
from builtins import list as _list


@curry
def take_last_while(predicate, list):
    """Returns a new list containing the last n elements of a given list, passing
    each value to the supplied predicate function, and terminating when the
    predicate function returns false. Excludes the element that caused the
    predicate function to fail. The predicate function is passed one argument:
    (value)"""
    for i, e in enumerate(reversed(list)):
        if not predicate(e):
            return list[-i:]
    return list
