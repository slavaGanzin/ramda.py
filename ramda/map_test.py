from ramda import *
from ramda.private.asserts import *


def add1(x):
    return x + 1


def map_nocurry_test():

    assert_iterables_equal(map(add1, [1, 2, 3]), [2, 3, 4])
    assert_iterables_equal(map(add1, {"a": 1, "b": 2}), {"a": 2, "b": 3})


def map_curry_test():
    assert_iterables_equal(map(add1)([1, 2, 3]), [2, 3, 4])
