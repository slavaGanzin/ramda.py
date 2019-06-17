from ramda.head import head
from ramda.private.asserts import *


def head_test():
    assert_equal(head([1, 2, 3]), 1)
    assert_equal(head("abc"), "a")
