from ramda import *
from ramda.private.asserts import *


def for_each_obj_indexed_test():
    pairs = []

    def obj_to_pairs(v, k):
        pairs.append([k, v])

    assert_equal(for_each_obj_indexed(obj_to_pairs, {"x": 1, "y": 2}), None)

    assert_equal(pairs, [["x", 1], ["y", 2]])

    pairs = []
    assert_equal(for_each_obj_indexed(obj_to_pairs, [1, 2]), None)

    assert_equal(pairs, [[0, 1], [1, 2]])
