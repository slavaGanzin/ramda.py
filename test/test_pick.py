from ramda import *
from ramda.private.asserts import *


test_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

expected_dict = {"b": 2, "d": 4}


def test_pick_nocurry():
    assert_dicts_equal(pick(["b", "d"], test_dict), expected_dict)


def test_pick_curry():
    assert_dicts_equal(pick(["b", "d"])(test_dict), expected_dict)
    assert_dicts_equal(pick(["there_is_no_key"])(test_dict), {})
