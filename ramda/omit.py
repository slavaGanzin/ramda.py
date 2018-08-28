from ramda.curry import curry


@curry
def omit(keys, dict):
    picked_dict = {}
    for k in keys:
        if k not in dict:
            picked_dict[k] = dict[k]
    return picked_dict
