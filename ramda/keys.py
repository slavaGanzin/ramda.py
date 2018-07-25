from ramda.curry import curry


@curry
def keys(dict):
    return dict.keys()
