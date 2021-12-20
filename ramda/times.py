"""This functions returns list from 1 to n"""


def times(function, n):
    return [function(i) for i in range(0, n)]
