from toolz import curry


@curry
def mean(xs):
    """Returns the mean of the given list of numbers"""
    return sum(xs) / len(xs)
