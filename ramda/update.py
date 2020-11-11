from toolz import curry


@curry
def update(i, v, xs):
    """Returns a new copy of the array with the element at the provided index
    replaced with the given value"""
    return [v if i == ind else x for ind, x in enumerate(xs)]
