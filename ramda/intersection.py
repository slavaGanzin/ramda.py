from toolz import curry


@curry
def intersection(list1, list2):
    """Combines two lists into a set (i.e. no duplicates) composed of those
    elements common to both lists"""
    return list(set(list1).intersection(set(list2)))
