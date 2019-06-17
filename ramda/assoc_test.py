from .assoc import assoc
from ramda.private.asserts import *


def assoc_nocurry_test():
    assert_equal(assoc("c", 3, {"a": 1, "b": 2}), {"a": 1, "b": 2, "c": 3})


def assoc_curry_test():
    assert_equal(assoc("c", 3)({"a": 1, "b": 2}), {"a": 1, "b": 2, "c": 3})
    assert_equal(assoc("c")(3, {"a": 1, "b": 2}), {"a": 1, "b": 2, "c": 3})
    assert_equal(assoc("c")(3)({"a": 1, "b": 2}), {"a": 1, "b": 2, "c": 3})
