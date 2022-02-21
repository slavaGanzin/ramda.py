from ramda import sum
from ramda.private.asserts import assert_equal


def test_sum():
    assert_equal(sum([1, 2, 3]), 6)
