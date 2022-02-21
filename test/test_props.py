from ramda.private.asserts import *
from ramda import *


def test_props():
    assert_equal(props(["x", "y"], {"x": 1, "y": 2}), [1, 2])
    assert_equal(props(["c", "a", "b"], {"b": 2, "a": 1}), [None, 1, 2])

    full_name = compose(join(" "), props(["first", "last"]))

    full_name({"last": "Bullet-Tooth", "age": 33, "first": "Tony"})

    assert_equal(
        full_name({"last": "Bullet-Tooth", "age": 33, "first": "Tony"}),
        "Tony Bullet-Tooth",
    )
