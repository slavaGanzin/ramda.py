from toolz import curry


@curry
def pick(keys, dict):
    """Returns a partial copy of an object containing only the keys specified. If
the key does not exist, the property is ignored"""
    picked_dict = {}
    for k in keys:
        if k in dict:
            picked_dict[k] = dict[k]
    return picked_dict
