from ramda.private.asserts import *
from .to_upper import to_upper


def to_upper_test():
    assert_equal(to_upper("abcdefgh"), "ABCDEFGH")
