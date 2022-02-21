from ramda import *
from ramda.private.asserts import *


def test_take_nocurry():
    assert_iterables_equal(take(2, [1, 2, 3, 4]), [1, 2])


def test_take_curry():
    assert_iterables_equal(take(2)([1, 2, 3, 4]), [1, 2])
    assert_iterables_equal(
        take(2)(({"a": 1, "b": 2, "c": 3}).items()), [("a", 1), ("b", 2)]
    )
