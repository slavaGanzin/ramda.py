from ramda.init import init
from ramda.private.asserts import *


def init_test():
    assert_equal(init([1, 2, 3]), [1, 2])
    assert_equal(init("abc"), "ab")
    assert_equal(init(""), "")
    assert_equal(init([]), [])
