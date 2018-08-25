from ramda.curry import curry
from ramda.clone import clone


@curry
def merge(object1, object2):
    result = clone(object1)
    for k, v in object2.items():
        result[k] = v

    return result
