from ramda.curry import curry


@curry
def insert(position, element, list):
    return list[:position] + [element] + list[position:]
