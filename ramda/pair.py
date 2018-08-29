from ramda.curry import curry


@curry
def pair(first, second):
    return [first, second]
