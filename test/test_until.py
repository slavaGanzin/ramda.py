from ramda import *
from ramda.private.asserts import *


def test_until():
    assert_equal(until(gt(100), multiply(2))(1), 128)
