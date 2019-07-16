from toolz import curry
from ramda.clone import clone


@curry
def merge_all(objects):
    """Merges a list of objects together into one object"""
    result = clone(objects[0])
    for object in objects[1:]:
        for k, v in object.items():
            result[k] = v

    return result
