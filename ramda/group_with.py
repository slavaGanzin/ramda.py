from toolz import curry
from ramda.is_empty import is_empty


@curry
def group_with(predicate, xs):
    """Takes a list and returns a list of lists where each sublist's elements are
    all satisfied pairwise comparison according to the provided function.
    Only adjacent elements are passed to the comparison function"""
    if is_empty(xs):
        return []

    out = []
    is_str = isinstance(xs, str)
    group = [xs[0]]

    for x in xs[1:]:
        if predicate(group[-1], x):
            group += [x]
        else:
            out.append("".join(group) if is_str else group)
            group = [x]

    out.append("".join(group) if is_str else group)

    return out
