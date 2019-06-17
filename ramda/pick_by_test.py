from ramda.pick_by import pick_by
from ramda.private.asserts import *


def is_upper_case(val, key):
    return key.upper() == key


def pick_by_test():
    assert_equal(
        pick_by(is_upper_case, {"a": 1, "b": 2, "A": 3, "B": 4}), {"A": 3, "B": 4}
    )
