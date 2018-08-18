from ramda.curry import curry


@curry
def invert_obj(object):
    if type(object) is dict:
        o = object.items()
    else:
        o = enumerate(object)

    out = {}
    for key, value in o:
        out[value] = key
    return out
