from .assoc_path import assoc_path
from ramda.private.asserts import assert_equal


def assoc_path_nocurry_test():
    assert_equal(
        assoc_path(["a", "b", "c"], 42, {"a": {"b": {"c": 0}}}), {"a": {"b": {"c": 42}}}
    )
    assert_equal(assoc_path(["a", "b", "c"], 42, {"a": 5}), {"a": {"b": {"c": 42}}})


def assoc_path_curry_test():
    assert_equal(assoc_path(["a", "b", "c"])(42)({"a": 5}), {"a": {"b": {"c": 42}}})
    assert_equal(assoc_path(["a", "b", "c"], 42)({"a": 5}), {"a": {"b": {"c": 42}}})
    assert_equal(assoc_path(["a", "b", "c"])(42, {"a": 5}), {"a": {"b": {"c": 42}}})
