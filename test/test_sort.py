from ramda import *
from ramda.private.asserts import *


def diff(a, b):
    return a - b


def test_sort():
    assert_equal(sort(diff, [4, 2, 7, 5]), [2, 4, 5, 7])
