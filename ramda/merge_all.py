from ramda.curry import curry
from ramda.clone import clone


@curry
def merge_all(objects):
    result = clone(objects[0])
    for object in objects[1:]:
        for k, v in object.items():
            result[k] = v

    return result
