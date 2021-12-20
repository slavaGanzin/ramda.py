from .update import update
from ramda.private.asserts import assert_iterables_equal


def cons_nocurry_test():
    assert_iterables_equal(update(1, 1, [2, 3]), [2, 1])
    assert_iterables_equal(update(-1, "_", ["a", "b", "c"]), ["a", "b", "_"])


def cons_curry_test():
    assert_iterables_equal(update(1, 1)([2, 3]), [2, 1])
