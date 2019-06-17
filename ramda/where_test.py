from ramda import *
from ramda.private.asserts import *

pred = where(
    {
        "a": equals("foo"),
        "b": complement(equals("bar")),
        "x": lambda x: x > 10,
        "y": lambda x: x < 20,
    }
)


def without_test():
    assert_equal(pred({"a": "foo", "b": "xxx", "x": 11, "y": 19}), True)
    assert_equal(pred({"a": "xxx", "b": "xxx", "x": 11, "y": 19}), False)
    assert_equal(pred({"a": "foo", "b": "bar", "x": 11, "y": 19}), False)
    assert_equal(pred({"a": "foo", "b": "xxx", "x": 10, "y": 19}), False)
    assert_equal(pred({"a": "foo", "b": "xxx", "x": 11, "y": 20}), False)
