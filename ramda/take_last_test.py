from ramda import *
from ramda.private.asserts import *


def take_test():
    assert_equal(take_last(1, ["foo", "bar", "baz"]), ["baz"])
    assert_equal(take_last(2, ["foo", "bar", "baz"]), ["bar", "baz"])
    assert_equal(take_last(3, ["foo", "bar", "baz"]), ["foo", "bar", "baz"])
    assert_equal(take_last(4, ["foo", "bar", "baz"]), ["foo", "bar", "baz"])
    assert_equal(take_last(3, "ramda"), "mda")
