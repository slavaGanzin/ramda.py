from ramda.private.asserts import *
from ramda.ends_with import ends_with


def ends_with_test():
    assert_equal(ends_with("c", "abc"), True)
    assert_equal(ends_with("b", "abc"), False)
    assert_equal(ends_with(["c"], ["a", "b", "c"]), True)
    assert_equal(ends_with(["b"], ["a", "b", "c"]), False)
