from ramda.pair import pair
from ramda.private.asserts import *


def pair_test():
    assert_equal(pair("foo", "bar"), ["foo", "bar"])
