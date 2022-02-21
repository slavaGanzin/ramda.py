from ramda.private.asserts import assert_iterables_equal
from ramda import xprod


def test_uniq_nocurry():
    assert_iterables_equal(
        xprod([1, 2], ["a", "b"]), [[1, "a"], [2, "a"], [1, "b"], [2, "b"]]
    )


def test_take_curry():
    assert_iterables_equal(
        xprod([1, 2])(["a", "b"]), [[1, "a"], [2, "a"], [1, "b"], [2, "b"]]
    )
