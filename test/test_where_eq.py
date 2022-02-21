from ramda import *
from ramda.private.asserts import *


pred = where_eq({"a": 1, "b": 2})


def test_where_eq():
    assert_equal(pred({"a": 1}), False)
    assert_equal(pred({"a": 1, "b": 2}), True)
    assert_equal(pred({"a": 1, "b": 2, "c": 3}), True)
    assert_equal(pred({"a": 1, "b": 1}), False)
