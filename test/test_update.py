from ramda import update
from ramda.private.asserts import assert_iterables_equal


def test_cons_nocurry():
    assert_iterables_equal(update(1, 1, [2, 3]), [2, 1])
    assert_iterables_equal(update(-1, "_", ["a", "b", "c"]), ["a", "b", "_"])


def test_cons_curry():
    assert_iterables_equal(update(1, 1)([2, 3]), [2, 1])
