from ramda.find_last import find_last
from ramda.private.asserts import assert_equal


def positive(x):
    return x > 0


def find_last_nocurry_test():
    assert_equal(find_last(positive, [-2, -1, 0, 1, 2, -2]), 2)


def find_last_curry_test():
    assert_equal(find_last(positive)([-2, -1, 0, 1, 2, -1, -2]), 2)


def not_found_test():
    assert_equal(find_last(positive, []), None)
