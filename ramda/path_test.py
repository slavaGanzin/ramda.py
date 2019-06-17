from .path import path
from ramda.private.asserts import assert_equal


test_dict = {"a": {"b": {"c": "foo"}}}


def path_nocurry_test():
    assert_equal(path(["a", "b", "c"], test_dict), "foo")


def path_curry_test():
    get_abc = path(["a", "b", "c"])
    assert_equal(get_abc(test_dict), "foo")


def path_throws_test():
    try:
        path([], test_dict)
    except ValueError:
        assert_equal(True, True)
