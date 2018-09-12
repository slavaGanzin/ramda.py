from ramda.curry import curry


@curry
def prepend(value, list):
    return [value] + list
