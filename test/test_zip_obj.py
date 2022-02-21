from ramda import zip_obj
from ramda.private.asserts import assert_iterables_equal


def test_uniq_nocurry():
    assert_iterables_equal(
        zip_obj(["a", "b", "c"], [1, 2, 3]), {"a": 1, "b": 2, "c": 3}
    )


def test_take_curry():
    assert_iterables_equal(
        zip_obj(["a", "b", "c"])([1, 2, 3]), {"a": 1, "b": 2, "c": 3}
    )
