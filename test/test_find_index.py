from ramda.find_index import find_index
from ramda.private.asserts import *


def positive(x):
    return x > 0


def test_find_index_nocurry():
    assert_equal(find_index(positive, [-2, -1, 0, 1, 2, -1, -2]), 3)


def test_find_index_curry():
    assert_equal(find_index(positive)([-2, -1, 0, 1, 2, -1, -2]), 3)


def test_not_found():
    assert_equal(find_index(positive, []), None)
