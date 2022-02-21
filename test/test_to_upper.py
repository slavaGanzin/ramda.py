from ramda.private.asserts import *
from ramda import to_upper


def test_to_upper():
    assert_equal(to_upper("abcdefgh"), "ABCDEFGH")
