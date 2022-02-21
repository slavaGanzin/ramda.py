from ramda import *
from ramda.private.asserts import *


def test_prop_satisfies():
    assert_equal(prop_satisfies(lt(0), "x", {"x": 1, "y": 2}), True)
