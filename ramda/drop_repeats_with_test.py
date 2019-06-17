from ramda.drop_repeats_with import drop_repeats_with
from ramda.private.asserts import *
from ramda.eq_by import eq_by


list = [1, -1, 1, 3, 4, -4, -4, -5, 5, 3, 3]


def drop_repeats_with_nocurry_test():
    assert_equal(drop_repeats_with(eq_by(abs), list), [1, 3, 4, -5, 3])
