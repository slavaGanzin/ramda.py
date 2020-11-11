from toolz import curry


@curry
def pick_all(keys, dict):
    """Similar to pick except that this one includes a key: undefined pair for
    properties that don't exist"""
    picked_dict = {}
    for k in keys:
        picked_dict[k] = None
        if k in dict:
            picked_dict[k] = dict[k]
    return picked_dict
