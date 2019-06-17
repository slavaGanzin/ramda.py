from ramda.last import last
from ramda.private.asserts import *


def last_test():
    assert_equal(last([1, 2, 3]), 3)
    assert_equal(last("abc"), "c")
