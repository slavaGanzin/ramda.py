from toolz import curry


@curry
def ends_with(needle, haystack):
    """Checks if a list ends with the provided values"""
    return haystack[-len(needle) :] == needle
