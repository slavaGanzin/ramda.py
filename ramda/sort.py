from toolz import curry
import functools


@curry
def sort(comparator, list):
    """Returns a copy of the list, sorted according to the comparator function,
    which should accept two values at a time and return a negative number if the
    first value is smaller, a positive number if it's larger, and zero if they
    are equal. Please note that this is a copy of the list. It does not
    modify the original"""
    return sorted(list, key=functools.cmp_to_key(comparator))
