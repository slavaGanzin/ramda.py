from ramda import *
from ramda.private.asserts import *


def is_not_four(x):
    return x is not 4


def take_while_test():
    assert_equal(take_while(is_not_four, [1, 2, 3, 4, 3, 2, 1]), [1, 2, 3])

    assert_equal(take_while(lambda x: x is not "d", "Ramda"), "Ram")
