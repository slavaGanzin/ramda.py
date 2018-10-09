from ramda import *
from ramda.private.asserts import *

xs = [1, 3, 5, 60, 777, 800]
ys = [2, 4, 6]


def is_odd(acc, x):
    return x % 2 == 1


def reduce_while_test():
    assert_equal(reduce_while(is_odd, add, 0, xs), 9)
    assert_equal(reduce_while(is_odd, add, 111, ys), 111)
