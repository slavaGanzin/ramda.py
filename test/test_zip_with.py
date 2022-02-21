from ramda import zip_with
from ramda.private.asserts import assert_iterables_equal


def add(a, b):
    return a + b


def test_uniq_nocurry():
    assert_iterables_equal(zip_with(add, [1, 1, 1], [1, 2, 3]), [2, 3, 4])


def test_take_curry():
    assert_iterables_equal(zip_with(add)([1, 1, 1], [1, 2, 3]), [2, 3, 4])
