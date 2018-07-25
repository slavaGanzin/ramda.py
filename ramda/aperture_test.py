from .aperture import aperture
from ramda.private.asserts import assert_iterables_equal


def aperture_nocurry_test():
    assert_iterables_equal(aperture(2, [1, 2, 3, 4, 5]), [[1, 2], [3, 4], [5]])


def aperture_curry_test():
    assert_iterables_equal(aperture(2)([1, 2, 3, 4, 5]), [[1, 2], [3, 4], [5]])


def aperture_curry_test():
    assert_iterables_equal(aperture(10)([1, 2, 3, 4, 5]), [])
