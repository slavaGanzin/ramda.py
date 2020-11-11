from toolz import curry
from ramda.clone import clone


@curry
def merge(object1, object2):
    """Create a new object with the own properties of the first object merged with
    the own properties of the second object. If a key exists in both objects,
    the value from the second object will be used"""
    result = clone(object1)
    for k, v in object2.items():
        result[k] = v

    return result
