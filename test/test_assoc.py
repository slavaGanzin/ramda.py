from ramda import assoc
from ramda.private.asserts import *


def test_assoc_nocurry():
    assert_equal(assoc("c", 3, {"a": 1, "b": 2}), {"a": 1, "b": 2, "c": 3})


def test_assoc_curry():
    assert_equal(assoc("c", 3)({"a": 1, "b": 2}), {"a": 1, "b": 2, "c": 3})
    assert_equal(assoc("c")(3, {"a": 1, "b": 2}), {"a": 1, "b": 2, "c": 3})
    assert_equal(assoc("c")(3)({"a": 1, "b": 2}), {"a": 1, "b": 2, "c": 3})
