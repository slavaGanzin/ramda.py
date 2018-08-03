from .binary import binary
from .private.asserts import assert_equal


def takes_three(x, y, z):
    return [x, y, z]


def takes_one(x):
    return x


def binary_test():
    assert_equal(binary(takes_three)(1, 2), [1, 2, None])

    binary(takes_one)
