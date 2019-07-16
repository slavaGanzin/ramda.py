from toolz import curry


@curry
def pair(first, second):
    """Takes two arguments, fst and snd, and returns [fst, snd]"""
    return [first, second]
