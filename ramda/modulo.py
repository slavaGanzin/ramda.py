from toolz import curry


@curry
def modulo(x, y):
    """Divides the first parameter by the second and returns the remainder. Note
    that this function preserves the JavaScript-style behavior for modulo. For
    mathematical modulo see mathMod"""
    return x % y
