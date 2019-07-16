from toolz import curry


@curry
def sort_by(comparator, list):
    """Sorts the list according to the supplied function"""
    return sorted(list, key=comparator)
