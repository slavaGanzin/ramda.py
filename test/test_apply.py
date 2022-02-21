from ramda import apply
from ramda import add
from ramda.private.asserts import assert_equal


def test_apply_nocurry():
    assert_equal(apply(add, [1, 2]), 3)


def test_apply_curry():
    assert_equal(apply(add)([1, 2]), 3)
