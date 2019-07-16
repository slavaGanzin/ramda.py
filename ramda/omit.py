from toolz import curry


@curry
def omit(keys, dict):
    """Returns a partial copy of an object omitting the keys specified"""
    picked_dict = {}
    for k in keys:
        if k not in dict:
            picked_dict[k] = dict[k]
    return picked_dict
