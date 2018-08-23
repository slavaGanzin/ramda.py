from ramda.max_by import max_by
from ramda.reduce import reduce
from ramda.private.asserts import *


def max_by_test():
    def square(n):
        return n * n

    assert_equal(max_by(square, -3, 2), -3)
    assert_equal(reduce(max_by(square), 0, [3, -5, 4, 1, -2]), -5)
    assert_equal(reduce(max_by(square), 0, []), 0)
