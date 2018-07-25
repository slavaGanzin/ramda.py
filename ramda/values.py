from ramda.curry import curry


@curry
def values(dict):
    return dict.values()
