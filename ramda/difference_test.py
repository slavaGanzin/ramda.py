from ramda.private.asserts import *
from ramda.difference import difference


def difference_test():
    assert_equal(difference([1, 2, 3, 4], [7, 6, 5, 4, 3]), [1, 2])
    assert_equal(difference([7, 6, 5, 4, 3], [1, 2, 3, 4]), [7, 6, 5])
    assert_equal(difference([{"a": 1}, {"b": 2}], [{"a": 1}, {"c": 3}]), [{"b": 2}])
    assert_equal(difference([1, 2, 1], [3]), [1, 2])
