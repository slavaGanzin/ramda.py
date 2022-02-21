from ramda.find_last import find_last
from ramda.private.asserts import assert_equal


def positive(x):
    return x > 0


def test_find_last_nocurry():
    assert_equal(find_last(positive, [-2, -1, 0, 1, 2, -2]), 2)


def test_find_last_curry():
    assert_equal(find_last(positive)([-2, -1, 0, 1, 2, -1, -2]), 2)


def test_not_found():
    assert_equal(find_last(positive, []), None)
