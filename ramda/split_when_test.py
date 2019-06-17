from ramda import *
from ramda.private.asserts import *


def split_when_test():
    assert_equal(split_when(equals(2), [1, 2, 3, 1, 2, 3]), [[1], [2, 3, 1, 2, 3]])
