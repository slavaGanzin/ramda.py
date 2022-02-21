from ramda import *
from ramda.private.asserts import *


def test_aperture_nocurry():
    assert_equal(aperture(2, [1, 2, 3, 4, 5]), [[1, 2], [2, 3], [3, 4], [4, 5]])
    assert_equal(
        aperture(2, [1, 2, 3, 4, 5, 6]), [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    )
    assert_equal(aperture(3, [1, 2, 3, 4, 5]), [[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    assert_equal(aperture(7, [1, 2, 3, 4, 5]), [])
