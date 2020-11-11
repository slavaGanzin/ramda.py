from toolz import curry


@curry
def inner_join(predicate, xs, ys):
    """Takes a predicate pred, a list xs, and a list ys, and returns a list
    xs' comprising each of the elements of xs which is equal to one or more
    elements of ys according to pred.
    pred must be a binary function expecting an element from each list.
    xs, ys, and xs' are treated as sets, semantically, so ordering should
    not be significant, but since xs' is ordered the implementation guarantees
    that its values are in the same order as they appear in xs. Duplicates are
    not removed, so xs' may contain duplicates if xs contains duplicates"""
    out = []
    for x in xs:
        for y in ys:
            if predicate(x, y):
                out.append(x)
    return out
