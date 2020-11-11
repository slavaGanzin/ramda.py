from toolz import curry


@curry
def unfold(iterator, seed):
    """Builds a list from a seed value. Accepts an iterator function, which returns
    either false to stop iteration or an array of length 2 containing the value
    to add to the resulting list and the seed to be used in the next call to the
    iterator function.
    The iterator function receives one argument: (seed)"""
    pair = iterator(seed)
    result = []
    while pair and (pair):
        result.append(pair[0])
        pair = iterator(pair[1])

    return result
