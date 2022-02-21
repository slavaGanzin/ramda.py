from ramda import *
from ramda.private.asserts import *


def test_split_when():
    assert_equal(split_when(equals(2), [1, 2, 3, 1, 2, 3]), [[1], [2, 3, 1, 2, 3]])
