from ramda.find_last_index import find_last_index
from ramda.private.asserts import *


def positive(x):
    return x > 0


def find_index_nocurry_test():
    assert_equal(find_last_index(positive, [-2, -1, 0, 1, 2, -2]), 5)


def find_index_curry_test():
    assert_equal(find_last_index(positive)([-2, -1, 0, 1, 2, -1]), 5)


def not_found_test():
    assert_equal(find_last_index(positive, []), None)
