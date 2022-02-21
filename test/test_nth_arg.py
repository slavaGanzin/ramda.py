from ramda.nth_arg import nth_arg
from ramda.private.asserts import *


def test_nth_arg():
    assert_equal(nth_arg(1)("a", "b", "c"), "b")
    assert_equal(nth_arg(-1)("a", "b", "c"), "c")
