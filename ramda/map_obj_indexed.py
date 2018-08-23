from ramda.curry import curry


@curry
def map_obj_indexed(f, dict):
    f_dict = {}
    for k, v in dict.items():
        f_dict[k] = f(v)
    return f_dict
