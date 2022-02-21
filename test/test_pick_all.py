from ramda import *
from ramda.private.asserts import *


def test_pick_all():
    assert_equal(
        pick_all(["a", "d"], {"a": 1, "b": 2, "c": 3, "d": 4}), {"a": 1, "d": 4}
    )
    assert_equal(
        pick_all(["a", "e", "f"], {"a": 1, "b": 2, "c": 3, "d": 4}),
        {"a": 1, "e": None, "f": None},
    )
