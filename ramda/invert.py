from ramda.curry import curry


@curry
def invert(object):
    if type(object) is dict:
        o = object.items()
    else:
        o = enumerate(object)

    out = {}
    for key, value in o:
        try:
            out[value].append(key)
        except KeyError:
            out[value] = [key]

    return out
