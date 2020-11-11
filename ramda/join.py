from toolz import curry


@curry
def join(sep, xs):
    """Returns a string made by inserting the separator between each element and
    concatenating all the elements into a single string"""
    return str(sep).join(xs)
