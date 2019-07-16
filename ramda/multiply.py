from toolz import curry


@curry
def multiply(x, y):
    """Multiplies two numbers. Equivalent to a * b but curried"""
    return x * y
