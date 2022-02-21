from ramda.clamp import clamp
from ramda.private.asserts import *


def test_clamp_curry():
    assert_equal(clamp(0)(1)(10), 1)
    assert_equal(clamp(0, 1)(0.1), 0.1)
    assert_equal(clamp(0, 1)(-1), 0)


def test_clamp_nocurry():
    assert_equal(clamp(0, 1, 10), 1)
    try:
        clamp(-10, -20, 10)
        assert False, "clamp(-10, -20, 10) must raise ValueError"
    except ValueError:
        pass
