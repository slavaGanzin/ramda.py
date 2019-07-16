from toolz import curry


@curry
def dec(x):
    """Decrements its argument"""
    return x - 1
