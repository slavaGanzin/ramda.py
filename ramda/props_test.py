from ramda import *
from ramda.private.asserts import *


def props_test():
    assert_equal(props(["x", "y"], {"x": 1, "y": 2}), [1, 2])
    assert_equal(props(["c", "a", "b"], {"b": 2, "a": 1}), [None, 1, 2])

    full_name = compose(join(" "), props(["first", "last"]))
    assert_equal(
        full_name({"last": "Bullet-Tooth", "age": 33, "first": "Tony"}),
        "Tony Bullet-Tooth",
    )
