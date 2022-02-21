from ramda import omit
from ramda.private.asserts import assert_dicts_equal


def test_pick_nocurry():
    assert_dicts_equal(
        omit(["a", "d"], {"a": 1, "b": 2, "c": 3, "d": 4}), {"b": 2, "c": 3}
    )

    assert_dicts_equal(
        omit(["there_is_no_key"], {"a": 1, "b": 2, "c": 3, "d": 4}),
        {"a": 1, "b": 2, "c": 3, "d": 4},
    )
