from ramda import path
from ramda.private.asserts import assert_equal


test_dict = {"a": {"b": {"c": "foo"}}}


def test_path_nocurry():
    assert_equal(path(["a", "b", "c"], test_dict), "foo")


def test_path_curry():
    get_abc = path(["a", "b", "c"])
    assert_equal(get_abc(test_dict), "foo")


def test_path_throws():
    try:
        path([], test_dict)
    except ValueError:
        assert_equal(True, True)
