from ramda import min
from ramda.private.asserts import assert_equal


def test_min():
    assert_equal(min(3, 1), 1)
