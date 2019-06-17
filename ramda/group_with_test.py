from ramda.group_with import group_with
from ramda.private.asserts import *
from ramda.equals import equals
from ramda.eq_by import eq_by


def is_vowel(x):
    return x in ["a", "e", "o", "y", "u", "i"]


def group_with_test():
    assert_equal(
        group_with(equals, [0, 1, 1, 2, 3, 5, 8, 13, 21]),
        [[0], [1, 1], [2], [3], [5], [8], [13], [21]],
    )

    assert_equal(
        group_with(lambda a, b: a + 1 == b, [0, 1, 1, 2, 3, 5, 8, 13, 21]),
        [[0, 1], [1, 2, 3], [5], [8], [13], [21]],
    )

    assert_equal(
        group_with(lambda a, b: a % 2 == b % 2, [0, 1, 1, 2, 3, 5, 8, 13, 21]),
        [[0], [1, 1], [2], [3, 5], [8], [13, 21]],
    )

    assert_equal(group_with(eq_by(is_vowel), "aestiou"), ["ae", "st", "iou"])
