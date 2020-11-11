from toolz import curry


@curry
def omit(keys, dict):
    """Returns a partial copy of an object omitting the keys specified"""
    picked_dict = {}
    for k in dict.keys():
        if k not in keys:
            picked_dict[k] = dict[k]
    return picked_dict
