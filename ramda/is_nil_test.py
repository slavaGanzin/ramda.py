from ramda.is_nil import is_nil
from ramda.private.asserts import *


def is_nil_test():
    assert_equal(is_nil(None), True)
    assert_equal(is_nil(0), False)
    assert_equal(is_nil([]), False)
