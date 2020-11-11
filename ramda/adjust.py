from toolz import curry


@curry
def adjust(f, i, xs):
    """Applies a function to the value at the given index of an array, returning a
    new copy of the array with the element at the given index replaced with the
    result of the function application"""
    return [f(x) if i == ind else x for ind, x in enumerate(xs)]
