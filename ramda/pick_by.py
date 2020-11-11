from toolz import curry


@curry
def pick_by(f, dict):
    """Returns a partial copy of an object containing only the keys that satisfy
    the supplied predicate"""
    picked_dict = {}
    for k, v in dict.items():
        if f(v, k):
            picked_dict[k] = v
    return picked_dict
