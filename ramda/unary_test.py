from ramda import *
from ramda.private.asserts import *


def takes_two_args(a, b):
    return [a, b]


takes_one_arg = unary(takes_two_args)


def unary_test():
    assert_equal(takes_two_args(1, 2), [1, 2])
    assert_equal(takes_one_arg(1), [1, None])
