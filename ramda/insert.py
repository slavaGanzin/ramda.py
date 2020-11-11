from toolz import curry


@curry
def insert(position, element, list):
    """Inserts the supplied element into the list, at the specified index. Note that
    this is not destructive: it returns a copy of the list with the changes.
    No lists have been harmed in the application of this function"""
    return list[:position] + [element] + list[position:]
