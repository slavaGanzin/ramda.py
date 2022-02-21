from ramda import lesser
from ramda.private.asserts import assert_equal


def test_lesser_nocurry():
    assert_equal(lesser(5, 3), 3)
    assert_equal(lesser(5, 7), 5)


def test_lesser_curry():
    max5 = lesser(5)
    assert_equal(max5(3), 3)
    assert_equal(max5(7), 5)
