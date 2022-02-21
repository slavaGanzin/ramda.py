from ramda import max
from ramda.private.asserts import assert_equal


def test_max():
    assert_equal(max(3, 4), 4)
