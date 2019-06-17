from ramda.private.asserts import *
from ramda import *


def split_every_test():
    assert_equal(split_every(3, [1, 2, 3, 4, 5, 6, 7]), [[1, 2, 3], [4, 5, 6], [7]])
    assert_equal(split_every(3, "foobarbaz"), ["foo", "bar", "baz"])
