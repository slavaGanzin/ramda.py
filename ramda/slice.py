from toolz import curry


@curry
def slice(from_index, to_index, list_or_string):
    """Returns the elements of the given list or string (or object with a slice
    method) from fromIndex (inclusive) to toIndex (exclusive).
    Dispatches to the slice method of the third argument, if present"""
    return list_or_string[from_index:to_index]
