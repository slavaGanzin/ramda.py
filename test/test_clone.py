from ramda import clone
from ramda.private.asserts import assert_equal, assert_dicts_equal


def test_clone():
    a = {"a": 1}
    b = clone(a)
    assert_dicts_equal(a, b)

    b["a"] = 2

    assert_equal(list(a.values()), [1])
    assert_equal(list(b.values()), [2])
