from toolz import curry


@curry
def split_when(predicate, list):
    """Takes a list and a predicate and returns a pair of lists with the following properties:
    the result of concatenating the two output lists is equivalent to the input list;
    none of the elements of the first output list satisfies the predicate; and
    if the second output list is non-empty, its first element satisfies the predicate"""
    for i, e in enumerate(list):
        if predicate(e):
            return [list[:i], list[i:]]

    return list
