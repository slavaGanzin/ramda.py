from ramda import uniq
from ramda.private.asserts import assert_iterables_equal


def test_uniq_nocurry():
    assert_iterables_equal(uniq([1, 2, 3, 3, 4]), [1, 2, 3, 4])
