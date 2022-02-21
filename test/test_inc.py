from ramda import inc
from ramda.private.asserts import assert_equal


def test_inc():
    assert_equal(inc(5), 6)
