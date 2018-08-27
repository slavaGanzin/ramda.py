from ramda.min_by import min_by
from ramda.reduce import reduce
from ramda.private.asserts import *


def max_by_test():
    def square(n):
        return n * n

    assert_equal(min_by(square, -3, 2), 2)
    assert_equal(reduce(min_by(square), 0, [3, -5, 4, 1, -2]), 0)
    assert_equal(reduce(min_by(square), 0, []), 0)
