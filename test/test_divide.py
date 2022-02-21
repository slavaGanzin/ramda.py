from ramda import divide
from ramda.private.asserts import assert_equal


def test_divide_nocurry():
    assert_equal(divide(10, 5), 2)


def test_divide_curry():
    assert_equal(divide(10)(5), 2)
