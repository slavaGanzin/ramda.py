from ramda import *
from ramda.private.asserts import *
import math


def slice_test():
    assert_equal(slice(1, 3, ["a", "b", "c", "d"]), ["b", "c"])
    assert_equal(slice(1, 100000, ["a", "b", "c", "d"]), ["b", "c", "d"])
    assert_equal(slice(0, -1, ["a", "b", "c", "d"]), ["a", "b", "c"])
    assert_equal(slice(-3, -1, ["a", "b", "c", "d"]), ["b", "c"])
    assert_equal(slice(0, 3, "ramda"), "ram")
