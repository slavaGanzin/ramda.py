from ramda import multiply
from ramda.private.asserts import assert_equal


def test_multiply_nocurry():
    assert_equal(multiply(3, 6), 18)


def test_multiply_curry():
    assert_equal(multiply(3)(6), 18)
