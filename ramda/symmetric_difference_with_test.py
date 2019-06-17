from ramda import *
from ramda.private.asserts import *


eq_a = eq_by(prop("a"))
l1 = [{"a": 1}, {"a": 2}, {"a": 3}, {"a": 4}]
l2 = [{"a": 3}, {"a": 4}, {"a": 5}, {"a": 6}]


def symmetric_difference_with_test():
    assert_equal(
        symmetric_difference_with(eq_a, l1, l2),
        [{"a": 1}, {"a": 2}, {"a": 5}, {"a": 6}],
    )
