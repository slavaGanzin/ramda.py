from .negate import negate
from ramda.private.asserts import assert_equal


def negate_test():
    assert_equal(negate(5), -5)
