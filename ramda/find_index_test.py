from ramda.find_index import find_index
from ramda.private.asserts import *


def positive(x):
    return x > 0


def find_index_nocurry_test():
    assert_equal(find_index(positive, [-2, -1, 0, 1, 2, -1, -2]), 3)


def find_index_curry_test():
    assert_equal(find_index(positive)([-2, -1, 0, 1, 2, -1, -2]), 3)


def not_found_test():
    assert_equal(find_index(positive, []), None)
