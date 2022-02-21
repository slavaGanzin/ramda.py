from ramda import dec
from ramda.private.asserts import assert_equal


def test_dec():
    assert_equal(dec(5), 4)
