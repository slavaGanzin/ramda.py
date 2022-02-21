from ramda.is_empty import is_empty
from ramda.private.asserts import *


def test_is_empty():
    assert_equal(is_empty([1, 2, 3]), False)
    assert_equal(is_empty([]), True)
    assert_equal(is_empty(""), True)
    assert_equal(is_empty(None), False)
    assert_equal(is_empty({}), True)
    assert_equal(is_empty({"length": 0}), False)
