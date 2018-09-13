def product(xs):
    """Multiplies together all the elements of a list"""
    result = xs[0]
    for x in xs[1:]:
        result *= x
    return result
