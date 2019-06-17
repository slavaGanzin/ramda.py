from ramda.dissoc import dissoc
from ramda.private.asserts import *


def dissoc_test():
    assert_equal(dissoc("b", {"a": 1, "b": 2, "c": 3}), {"a": 1, "c": 3})


def dissoc_curry_test():
    assert_equal(dissoc("b")({"a": 1, "b": 2, "c": 3}), {"a": 1, "c": 3})
