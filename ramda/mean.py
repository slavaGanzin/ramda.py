from toolz import curry


@curry
def mean(xs):
    """Returns the mean of the given list of numbers"""
    try:
        return sum(xs) / len(xs)
    except ZeroDivisionError:
        return None
