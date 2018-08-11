from ramda.find import find
from ramda.private.asserts import assert_equal


def positive(x):
    return x > 0


def find_nocurry_test():
    assert_equal(find(positive, [-2, -1, 0, 1, 2]), 1)


def find_curry_test():
    assert_equal(find(positive)([-2, -1, 0, 1, 2]), 1)


def not_found_test():
    assert_equal(find(positive, []), None)
