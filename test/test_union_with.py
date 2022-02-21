from ramda import *
from ramda.private.asserts import *

l1 = [{"a": 1}, {"a": 2}]
l2 = [{"a": 1}, {"a": 4}]


def test_union_with():
    assert_equal(union_with(eq_by(prop("a")), l1, l2), [{"a": 1}, {"a": 2}, {"a": 4}])
