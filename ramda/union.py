from toolz import curry


@curry
def union(X, Y):
    """Combines two lists into a set (i.e. no duplicates) composed of the elements
    of each list"""
    return list(set(X + Y))
