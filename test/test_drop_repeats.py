from ramda.drop_repeats import drop_repeats
from ramda.private.asserts import *


def test_drop_repeats_nocurry():
    assert_equal(drop_repeats([1, 1, 1, 2, 3, 4, 4, 2, 2]), [1, 2, 3, 4, 2])
