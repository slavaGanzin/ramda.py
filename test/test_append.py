from ramda import append
from ramda.private.asserts import assert_iterables_equal


def test_append_nocurry():
    assert_iterables_equal(append(3, [1, 2]), [1, 2, 3])


def test_append_curry():
    assert_iterables_equal(append(3)([1, 2]), [1, 2, 3])
