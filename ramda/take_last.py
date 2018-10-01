from ramda.curry import curry


@curry
def take_last(n, list):
    """Returns a new list containing the last n elements of the given list.
If n > list.length, returns a list of list.length elements"""
    return list[-n:]
