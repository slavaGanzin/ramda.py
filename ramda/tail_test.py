from ramda.tail import tail
from ramda.private.asserts import *


def tail_test():
    assert_equal(tail([1, 2, 3]), [2, 3])
    assert_equal(tail("abc"), "bc")
    assert_equal(tail(""), "")
    assert_equal(tail([]), [])
