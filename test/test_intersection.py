from ramda.intersection import intersection
from ramda.private.asserts import *


def test_intersection():
    assert_equal(intersection([1, 2, 3, 4, 4], [7, 6, 5, 4, 3, 4]), [3, 4])
