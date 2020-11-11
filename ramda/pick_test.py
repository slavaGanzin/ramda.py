from ramda import *
from ramda.private.asserts import *


test_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

expected_dict = {"b": 2, "d": 4}


def pick_nocurry_test():
    assert_dicts_equal(pick(["b", "d"], test_dict), expected_dict)


def pick_curry_test():
    assert_dicts_equal(pick(["b", "d"])(test_dict), expected_dict)
    assert_dicts_equal(pick(["there_is_no_key"])(test_dict), {})
