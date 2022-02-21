from ramda import negate
from ramda.private.asserts import assert_equal


def test_negate():
    assert_equal(negate(5), -5)
