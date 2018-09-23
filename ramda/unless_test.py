from ramda import *
from ramda.private.asserts import *

safe_inc = unless(is_nil, inc)


def unless_test():
    assert_equal(safe_inc(None), None)
    assert_equal(safe_inc(1), 2)
