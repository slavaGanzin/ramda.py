from .curry import curry


@curry
def juxt(fs, args):
    return [f(*args) for f in fs]
