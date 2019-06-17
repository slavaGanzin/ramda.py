from ramda.private.asserts import *
from ramda.eq_props import eq_props


o1 = {"a": 1, "b": 2, "c": 3, "d": 4}
o2 = {"a": 10, "b": 20, "c": 3, "d": 40}


def eq_props_test():
    assert_equal(eq_props("a", o1, o2), False)
    assert_equal(eq_props("c", o1, o2), True)
