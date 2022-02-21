from ramda import *
from ramda.private.asserts import *


def test_split_at():
    assert_equal(split_at(1, [1, 2, 3]), [[1], [2, 3]])
    assert_equal(split_at(5, "hello world"), ["hello", " world"])
    assert_equal(split_at(-1, "foobar"), ["fooba", "r"])
