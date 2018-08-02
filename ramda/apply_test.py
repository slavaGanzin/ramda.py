from .apply import apply
from .add import add
from ramda.private.asserts import assert_equal


def apply_nocurry_test():
    assert_equal(apply(add, [1, 2]), 3)


def apply_curry_test():
    assert_equal(apply(add)([1, 2]), 3)
