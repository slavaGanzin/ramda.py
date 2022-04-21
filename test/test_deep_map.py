from ramda import *
from ramda.private.asserts import assert_equal


def test_deep_map():
    def add_one(x):
        if is_(int, x):
            return x + 1
        return x

    assert_equal(deep_map(add_one, {"a": 1, "b": {"c": 3}}), {"a": 2, "b": {"c": 4}})
    assert_equal(deep_map(add_one)({"a": 1, "b": {"c": 3}}), {"a": 2, "b": {"c": 4}})
