from ramda import *
from ramda.private.asserts import *


def unfold_test():
    def f(n):
        return False if n > 50 else [-n, n + 10]

    assert_equal(unfold(f, 10), [-10, -20, -30, -40, -50])
