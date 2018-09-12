def product(xs):
    result = xs[0]
    for x in xs[1:]:
        result *= x
    return result
