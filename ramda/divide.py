from toolz import curry


@curry
def divide(x, y):
    """Divides two numbers. Equivalent to a / b"""
    return x / y
