from ramda import *
from ramda.private.asserts import *


def prop_satisfies_test():
    assert_equal(prop_satisfies(lt(2), "x", {"x": 1, "y": 2}), True)
