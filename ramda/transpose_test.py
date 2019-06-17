from ramda.private.asserts import *
from ramda import *


def transpose_test():
    assert_equal(
        transpose([[1, "a"], [2, "b"], [3, "c"]]), [[1, 2, 3], ["a", "b", "c"]]
    )
    assert_equal(
        transpose([[1, 2, 3], ["a", "b", "c"]]), [[1, "a"], [2, "b"], [3, "c"]]
    )

    # assert_equal(
    #     transpose([[10, 11], [20], [], [30, 31, 32]]),
    #     [[10, 20, 30], [11, 31], [32]])
