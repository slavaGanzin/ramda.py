from ramda import greater
from ramda.private.asserts import assert_equal


def test_greater_nocurry():
    assert_equal(greater(5, 3), 5)
    assert_equal(greater(5, 7), 7)


def test_greater_curry():
    min5 = greater(5)
    assert_equal(min5(3), 5)
    assert_equal(min5(7), 7)
