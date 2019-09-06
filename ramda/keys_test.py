from .keys import keys
from ramda.private.asserts import assert_equal


test_dict = {"a": 1, "b": 2, "c": 3}


def keys_test():
    assert_equal(keys(test_dict), ["a", "b", "c"])
