from ramda import concat
from ramda.private.asserts import assert_iterables_equal


def test_concat_nocurry():
    assert_iterables_equal(concat([1, 2], [3, 4]), [1, 2, 3, 4])


def test_concat_curry():
    assert_iterables_equal(concat([1, 2])([3, 4]), [1, 2, 3, 4])


def test_concat_set():
    assert_iterables_equal(concat({1, 2})({3, 4}), [1, 2, 3, 4])
    assert_iterables_equal(concat({1, 2})([3, 4]), [1, 2, 3, 4])
    assert_iterables_equal(concat([1, 2])({3, 4}), [1, 2, 3, 4])
