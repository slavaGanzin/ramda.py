from ramda.drop_repeats import drop_repeats
from ramda.private.asserts import *


def drop_repeats_nocurry_test():
    assert_equal(drop_repeats([1, 1, 1, 2, 3, 4, 4, 2, 2]), [1, 2, 3, 4, 2])
