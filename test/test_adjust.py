from ramda import adjust
from ramda import to_upper
from ramda.private.asserts import assert_iterables_equal


def add_one(x):
    return x + 1


def test_cons_nocurry():
    assert_iterables_equal(adjust(1, add_one, [2, 3]), [2, 4])
    assert_iterables_equal(
        adjust(-1, to_upper, ["a", "b", "c", "d"]), ["a", "b", "c", "D"]
    )


def test_cons_curry():
    assert_iterables_equal(adjust(1, add_one)([2, 3]), [2, 4])
