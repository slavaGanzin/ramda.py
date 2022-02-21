from ramda.private.asserts import *
from ramda import length


def test_length():
    assert_equal(length([1, 2, 3]), 3)
    assert_equal(length("123"), 3)
