from ramda.private.asserts import *
from ramda.difference_with import difference_with
from ramda.complement import complement


l1 = [{"a": 1}, {"a": 2}, {"a": 3}]
l2 = [{"a": 3}, {"a": 4}]


def cmp(x, y):
    return x["a"] == y["a"]


def difference_with_test():
    assert_equal(difference_with(cmp, l1, l2), [{"a": 1}, {"a": 2}])
    assert_equal(difference_with(cmp, l1, l1), [])
    assert_equal(difference_with(cmp, l2, l1), [{"a": 4}])


def difference_with_curry_test():
    assert_equal(difference_with(complement(cmp))(l1, l1), [])
    assert_equal(difference_with(cmp)(l2)(l1), [{"a": 4}])
