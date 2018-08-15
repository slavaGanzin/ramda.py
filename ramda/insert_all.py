from ramda.curry import curry


@curry
def insert_all(position, elements, list):
    return list[:position] + elements + list[position:]
