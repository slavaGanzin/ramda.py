from ramda import *
from ramda.private.asserts import *


def test_use_with():
    assert_equal(use_with(pow, [identity, identity])(3, 4), 81)
    assert_equal(use_with(pow, [identity, identity])(3)(4), 81)
    assert_equal(use_with(pow, [dec, inc])(3, 4), 32)
    assert_equal(use_with(pow, [dec, inc])(3)(4), 32)

    assert_equal(use_with(pow, [lambda x: x - 1, inc])(3, 4), 32)
    assert_equal(use_with(lambda x, y: x + y, [identity, identity])(1, 2), 3)
