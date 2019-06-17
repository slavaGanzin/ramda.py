from ramda import *
from ramda.private.asserts import *


def to_pairs_test():
    assert_equal(to_pairs({"a": 1, "b": 2, "c": 3}), [["a", 1], ["b", 2], ["c", 3]])
