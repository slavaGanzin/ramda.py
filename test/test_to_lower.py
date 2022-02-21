from ramda.private.asserts import *
from ramda import to_lower


def test_to_upper():
    assert_equal(to_lower("ABCDEFGH"), "abcdefgh")
