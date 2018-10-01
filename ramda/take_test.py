from ramda import *
from ramda.private.asserts import *


def take_nocurry_test():
    assert_iterables_equal(take(2, [1, 2, 3, 4]), [1, 2])


def take_curry_test():
    assert_iterables_equal(take(2)([1, 2, 3, 4]), [1, 2])
