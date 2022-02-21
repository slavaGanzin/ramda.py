from ramda import assoc_path
from ramda.private.asserts import assert_equal


def test_assoc_path_nocurry():
    assert_equal(
        assoc_path(["a", "b", "c"], 42, {"a": {"b": {"c": 0}}}), {"a": {"b": {"c": 42}}}
    )
    assert_equal(assoc_path(["a", "b", "c"], 42, {"a": 5}), {"a": {"b": {"c": 42}}})


def test_assoc_path_curry():
    assert_equal(assoc_path(["a", "b", "c"])(42)({"a": 5}), {"a": {"b": {"c": 42}}})
    assert_equal(assoc_path(["a", "b", "c"], 42)({"a": 5}), {"a": {"b": {"c": 42}}})
    assert_equal(assoc_path(["a", "b", "c"])(42, {"a": 5}), {"a": {"b": {"c": 42}}})
