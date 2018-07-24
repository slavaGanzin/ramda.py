from ramda.function import curry
from ramda.iterable import map


@curry
def map_dict(f, dict):
    f_dict = {}
    for k, v in dict.items():
        f_dict[k] = f(v)
    return f_dict
