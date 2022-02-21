from ramda import *
from ramda.private.asserts import *
from numbers import Number


def test_prop_is():
    assert_equal(prop_is(Number, "x", {"x": 1, "y": 2}), True)
    assert_equal(prop_is(Number, "x", {"x": "foo"}), False)
    assert_equal(prop_is(Number, "x", {}), False)
