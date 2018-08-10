from ramda.curry import curry


@curry
def default_to(default, x):
    return default if x is None else x
