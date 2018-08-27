from ramda.none import none
from ramda.private.asserts import *


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 1


def none_test():
    assert_equal(none(is_even, [1, 3, 5, 7, 9, 11]), True)
    assert_equal(none(is_odd, [1, 3, 5, 7, 8, 11]), False)
