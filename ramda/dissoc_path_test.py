from ramda.dissoc_path import dissoc_path
from ramda.private.asserts import *


def dissoc_test():
    assert_equal(dissoc_path(["b"], {"a": 1, "b": 2, "c": 3}), {"a": 1, "c": 3})

    assert_equal(dissoc_path(["a", "b", "c"], {"a": {"b": {"c": 3}}}), {"a": {"b": {}}})


def dissoc_curry_test():
    assert_equal(dissoc_path(["b"])({"a": 1, "b": 2, "c": 3}), {"a": 1, "c": 3})
