from .times import times
from .identity import identity
from ramda.private.asserts import assert_iterables_equal


def uniq_nocurry_test():
    assert_iterables_equal(times(identity, 5), [0, 1, 2, 3, 4])
    assert_iterables_equal(times(identity)(5), [0, 1, 2, 3, 4])
