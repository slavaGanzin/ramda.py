from ramda.mean import mean
from ramda.private.asserts import assert_equal


def mean_test():
    assert_equal(mean([3, 5, 7]), 5)
    assert_equal(mean([5, 7, 3]), 5)
    assert_equal(mean([]), None)
