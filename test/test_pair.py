from ramda.pair import pair
from ramda.private.asserts import *


def test_pair():
    assert_equal(pair("foo", "bar"), ["foo", "bar"])
