from ramda.last import last
from ramda.private.asserts import *


def test_last():
    assert_equal(last([1, 2, 3]), 3)
    assert_equal(last("abc"), "c")
