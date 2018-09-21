from ramda import *
from ramda.private.asserts import *


def union_test():
    assert_equal(union([1, 2, 3], [2, 3, 4]), [1, 2, 3, 4])
