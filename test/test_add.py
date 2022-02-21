from ramda import add
from ramda.private.asserts import assert_equal


def test_add_nocurry():
    assert_equal(add(1, 2), 3)


def test_add_curry():
    assert_equal(add(1)(2), 3)
