from ramda.private.asserts import assert_iterables_equal
from ramda import without


def test_uniq_nocurry():
    assert_iterables_equal(without([1, 2], [1, 2, 1, 3, 4]), [3, 4])


def test_take_curry():
    assert_iterables_equal(without([1, 2])([1, 2, 1, 3, 4]), [3, 4])
