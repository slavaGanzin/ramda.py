from .curry import curry


@curry
def apply_to(x, f):
    return f(x)
