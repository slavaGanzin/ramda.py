from ramda.private.asserts import *
from .to_lower import to_lower


def to_upper_test():
    assert_equal(to_lower("ABCDEFGH"), "abcdefgh")
