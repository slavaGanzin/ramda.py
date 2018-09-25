from ramda import *
from ramda.private.asserts import *


def unnest_test():
    assert_equal(unnest([[1], [2], [[3]]]), [1, 2, [3]])
    assert_equal(unnest([[1, 2], [3, 4], [5, 6]]), [1, 2, 3, 4, 5, 6])
