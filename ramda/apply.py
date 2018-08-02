from .curry import curry


@curry
def apply(f, xs):
    return f(*xs)
