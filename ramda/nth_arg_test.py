from ramda.nth_arg import nth_arg
from ramda.private.asserts import *


def nth_arg_test():
    assert_equal(nth_arg(1)("a", "b", "c"), "b")
    assert_equal(nth_arg(-1)("a", "b", "c"), "c")
