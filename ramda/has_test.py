from ramda.has import has
from ramda.private.asserts import *


def has_test():
    has_name = has("name")
    assert_equal(has_name({"name": "alice"}), True)
    assert_equal(has_name({"name": "bob"}), True)
    assert_equal(has_name({}), False)

    point = {"x": 0, "y": 0}
    assert_equal(has("x", point), True)
    assert_equal(has("y", point), True)
    assert_equal(has("z", point), False)

    class X:
        def __init__(self):
            self.x = 1

    x = X()
    assert_equal(has("z", x), False)
    assert_equal(has("x", x), True)
