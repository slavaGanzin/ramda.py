from ramda.nth import nth
from ramda.private.asserts import *


list = ["foo", "bar", "baz", "quux"]


def nth_test():
    assert_equal(nth(1, list), "bar")
    assert_equal(nth(-1, list), "quux")
    assert_equal(nth(-99, list), None)

    assert_equal(nth(2, "abc"), "c")
    assert_equal(nth(3, "abc"), "")
