from ramda.dissoc import dissoc
from ramda.private.asserts import *


def test_dissoc():
    assert_equal(dissoc("b", {"a": 1, "b": 2, "c": 3}), {"a": 1, "c": 3})


def test_dissoc_curry():
    assert_equal(dissoc("b")({"a": 1, "b": 2, "c": 3}), {"a": 1, "c": 3})
