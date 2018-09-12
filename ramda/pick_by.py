from ramda.curry import curry


@curry
def pick_by(f, dict):
    picked_dict = {}
    for k, v in dict.items():
        if f(v, k):
            picked_dict[k] = v
    return picked_dict
