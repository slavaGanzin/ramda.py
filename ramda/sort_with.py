from toolz import curry
import functools


@curry
def sort_with(comparators, list):
    """Sorts a list according to a list of comparators"""

    def comparator(a, b):
        for c in comparators:
            result = c(a, b)
            if result is not 0:
                return result

        return 0

    return sorted(list, key=functools.cmp_to_key(comparator))
