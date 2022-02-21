from ramda import times
from ramda import identity
from ramda.private.asserts import assert_iterables_equal


def test_uniq_nocurry():
    assert_iterables_equal(times(identity, 5), [0, 1, 2, 3, 4])
    assert_iterables_equal(times(identity)(5), [0, 1, 2, 3, 4])
