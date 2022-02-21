from ramda import *
from ramda.private.asserts import *


def test_symmetric_difference():
    assert_equal(symmetric_difference([1, 2, 3, 4], [7, 6, 5, 4, 3]), [1, 2, 7, 6, 5])
    assert_equal(symmetric_difference([7, 6, 5, 4, 3], [1, 2, 3, 4]), [7, 6, 5, 1, 2])
