from ramda.private.asserts import *
from ramda import *


def range_test():
    assert_equal(range(1, 5), [1, 2, 3, 4])
    assert_equal(range(50, 53), [50, 51, 52])
