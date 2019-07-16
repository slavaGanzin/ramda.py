from toolz import curry


@curry
def subtract(x, y):
    """Subtracts its second argument from its first argument"""
    return x - y
