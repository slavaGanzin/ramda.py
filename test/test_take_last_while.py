from ramda import *
from ramda.private.asserts import *


def is_not_one(x):
    return x != 1


def test_take_last_while():
    assert_equal(take_last_while(is_not_one, [1, 2, 3, 4]), [2, 3, 4])

    assert_equal(take_last_while(lambda x: x != "R", "Ramda"), "amda")
