from ramda.curry_n import curry_n
from ramda.private.asserts import *


def f(x, y, z=3):
    return x + y + z


def run_f_curry_cases(fc):
    f4 = curry_n(4, f)
    assert_equal(f4(1, 1)(1, 1), 3)
    f2 = curry_n(2, f)
    try:
        f2(1, 2)
        assert False, 'Should raise'
    except TypeError:
        pass

    # assert_equal(fc(1, 1), 5)
    # assert_equal(fc(1)(1), 5)
