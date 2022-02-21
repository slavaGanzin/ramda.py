from ramda import *
from ramda.private.asserts import *


def is_not_four(x):
    return x != 4


def test_take_while():
    assert_equal(take_while(is_not_four, [1, 2, 3, 4, 3, 2, 1]), [1, 2, 3])

    assert_equal(take_while(lambda x: x != "d", "Ramda"), "Ram")
