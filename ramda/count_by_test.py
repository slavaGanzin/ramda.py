from ramda.private.asserts import *
from math import floor
from ramda.count_by import count_by
from ramda.to_lower import to_lower


def numbers_test():
    numbers = [1.0, 1.1, 1.2, 2.0, 3.0, 2.2]
    assert_equal(count_by(floor)(numbers), {1: 3, 2: 2, 3: 1})


def letter_test():
    letters = ["a", "b", "A", "a", "B", "c"]
    assert_equal(count_by(to_lower)(letters), {"a": 3, "b": 2, "c": 1})
