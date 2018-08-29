from ramda.private.asserts import *
from ramda.once import once
from ramda.add import add


add_one_once = once(add(1))


def once_test():
    assert_equal(add_one_once(10), 11)
    assert_equal(add_one_once(add_one_once(50)), 11)
