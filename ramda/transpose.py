from ramda.map import map
from builtins import list as tuple_to_list


def transpose(list):
    """Transposes the rows and columns of a 2D list.
    When passed a list of n lists of length x,
    returns a list of x lists of length n"""
    return [tuple_to_list(x) for x in zip(*list)]
