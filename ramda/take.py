from toolz import curry


@curry
def take(n, list):
    """Returns the first n elements of the given list, string, or
transducer/transformer (or object with a take method).
Dispatches to the take method of the second argument, if present"""
    acc = []

    if isinstance(list, str):
        return list[:n]

    if len(list) <= n:
        return list

    i = 0
    for e in list:
        i += 1
        if i > n:
            return acc
        acc.append(e)
