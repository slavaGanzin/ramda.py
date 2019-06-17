from ramda.drop_last_while import drop_last_while
from ramda.private.asserts import *


def lte_three(x):
    return x <= 3


def drop_last_while_nocurry_test():
    assert_equal(drop_last_while(lte_three, [1, 2, 3, 4, 3, 2, 1]), [1, 2, 3, 4])
    assert_equal(drop_last_while(lambda x: x != "d", "Ramda"), "Ramd")
