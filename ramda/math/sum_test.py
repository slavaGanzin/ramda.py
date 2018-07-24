from .sum import sum
from ramda.private.asserts import assert_equal


def sum_test():
    assert_equal(sum([1, 2, 3]), 6)
