from .curry import curry


@curry
def apply(f, xs):
    """Applies function fn to the argument list args. This is useful for
    creating a fixed-arity function from a variadic function. fn should be a
    bound function if context is significant"""
    return f(*xs)
