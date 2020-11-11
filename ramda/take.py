from toolz import curry


@curry
def take(n, list):
    """Returns the first n elements of the given list, string, or
    transducer/transformer (or object with a take method).
    Dispatches to the take method of the second argument, if present"""
    acc = []

    if isinstance(list, str):
        return list[:n]

    i = 0
    for e in list:
        if i >= n:
            return acc
        i += 1
        acc.append(e)

    return acc
