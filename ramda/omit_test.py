from .omit import omit
from ramda.private.asserts import assert_dicts_equal


def pick_nocurry_test():
    assert_dicts_equal(
        omit(["a", "d"], {"a": 1, "b": 2, "c": 3, "d": 4}), {"b": 2, "c": 3}
    )
