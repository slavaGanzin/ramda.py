from toolz import curry


def scan(function, accumulator, list):
    """Scan is similar to reduce, but returns a list of successively
    reduced values from the left"""
    result = [accumulator]
    for x in list:
        accumulator = function(accumulator, x)
        result.append(accumulator)

    return result
