from ramda.curry_n import curry_n
from ramda.private.asserts import *


def f(x, y, z=3):
    return x + y + z


def test_f4():
    f4 = curry_n(4, f)
    assert_equal(f4(1, 1)(1, 1), 3)


def test_f2():
    f2 = curry_n(2, f)
    try:
        f2(1, 2)
        assert_equal(False, "Should raise")
    except TypeError:
        pass
