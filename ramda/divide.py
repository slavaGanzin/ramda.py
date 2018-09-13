from ramda.curry import curry


@curry
def divide(x, y):
    """Divides two numbers. Equivalent to a / b"""
    return x / y
