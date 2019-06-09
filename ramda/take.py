from ramda.curry import curry


@curry
def take(n, list):
    """Returns the first n elements of the given list, string, or
transducer/transformer (or object with a take method).
Dispatches to the take method of the second argument, if present"""
    a = []
    i = 1
    for x in list:
        if i > n:
            return a
        a.append(x)
        i += 1
