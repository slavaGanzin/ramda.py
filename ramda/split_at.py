from toolz import curry


@curry
def split_at(index, list):
    """Splits a given list or string at a given index"""
    return [list[:index]] + [list[index:]]
