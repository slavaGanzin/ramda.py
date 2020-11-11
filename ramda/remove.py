from toolz import curry


@curry
def remove(index, length, list):
    """Removes the sub-list of list starting at index start and containing
    count elements. Note that this is not destructive: it returns a copy of
    the list with the changes.
    No lists have been harmed in the application of this function"""
    return list[:index] + list[index + length :]
