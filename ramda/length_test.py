from ramda.private.asserts import *
from .length import length


def length_test():
    assert_equal(length([1, 2, 3]), 3)
    assert_equal(length("123"), 3)
