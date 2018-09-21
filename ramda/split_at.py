from ramda.curry import curry


@curry
def split_at(index, string):
    """Splits a given list or string at a given index"""
    return [string[:index]] + [string[index:]]
