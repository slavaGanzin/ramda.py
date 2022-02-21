from ramda.median import median
from ramda.private.asserts import assert_equal


def test_median():
    assert_equal(median([2, 9, 7]), 7)
    assert_equal(median([7, 2, 10, 9]), 8)
    assert_equal(median([]), None)
