from ramda.curry import curry


@curry
def map_obj_indexed(f, dict):
    """An Object-specific version of map. The function is applied to three
arguments: (value, key, obj). If only the value is significant, use
map instead"""
    f_dict = {}
    for k, v in dict.items():
        f_dict[k] = f(v)
    return f_dict
