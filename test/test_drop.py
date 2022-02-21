from ramda import drop
from ramda.private.asserts import assert_iterables_equal


def test_drop_nocurry():
    assert_iterables_equal(drop(2, [1, 2, 3, 4]), [3, 4])


def test_drop_curry():
    assert_iterables_equal(drop(2)([1, 2, 3, 4]), [3, 4])
