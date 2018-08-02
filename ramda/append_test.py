from .append import append
from ramda.private.asserts import assert_iterables_equal


def append_nocurry_test():
    assert_iterables_equal(append(3, [1, 2]), [1, 2, 3])


def append_curry_test():
    assert_iterables_equal(append(3)([1, 2]), [1, 2, 3])
