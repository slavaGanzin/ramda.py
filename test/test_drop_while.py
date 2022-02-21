from ramda.drop_while import drop_while
from ramda.private.asserts import *


def lte_two(x):
    return x <= 2


def test_drop_while_nocurry():
    assert_equal(drop_while(lte_two, [1, 2, 3, 4, 3, 2, 1]), [3, 4, 3, 2, 1])
    assert_equal(drop_while(lambda x: x != "d", "Ramda"), "da")
