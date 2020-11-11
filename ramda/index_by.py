from toolz import curry


@curry
def index_by(f, xs):
    """Given a function that generates a key, turns a list of objects into an
    object indexing the objects by the given key. Note that if multiple
    objects generate the same value for the indexing key only the last value
    will be included in the generated object.
    Acts as a transducer if a transformer is given in list position"""
    out = {}
    for x in xs:
        out[f(x)] = x

    return out
