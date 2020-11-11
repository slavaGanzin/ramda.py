from .curry import curry


@curry
def apply_to(x, f):
    """Takes a value and applies a function to it.
    This function is also known as the thrush combinator"""
    return f(x)
