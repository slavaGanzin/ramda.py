from ramda.filter import filter
from ramda.private.asserts import assert_equal


def positive(x):
    return x > 0


def is_even(n):
    return n % 2 == 0


def filter_test():
    assert_equal(filter(positive, [2, -1, 0, 3, -2]), [2, 3])
    assert_equal(filter(positive)([2, -1, 0, 3, -2]), [2, 3])
    assert_equal(filter(positive)(123), [])
    assert_equal(filter(is_even, {"a": 1, "b": 2, "c": 3, "d": 4}), {"b": 2, "d": 4})
