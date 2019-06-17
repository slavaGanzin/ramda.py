from ramda.clamp import clamp
from ramda.private.asserts import *


def clamp_curry_test():
    assert_equal(clamp(0)(1)(10), 1)
    assert_equal(clamp(0, 1)(0.1), 0.1)
    assert_equal(clamp(0, 1)(-1), 0)


def clamp_nocurry_test():
    assert_equal(clamp(0, 1, 10), 1)
    try:
        clamp(-10, -20, 10)
        assert False, "clamp(-10, -20, 10) must raise ValueError"
    except ValueError:
        pass
