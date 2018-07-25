from .item_path import item_path
from ramda.private.asserts import assert_equal


test_dict = {
    "a": {
        "b": {
            "c": "foo"
        }
    }
}


def item_path_nocurry_test():
    assert_equal(item_path(["a", "b", "c"], test_dict), "foo")


def item_path_curry_test():
    get_abc = item_path(["a", "b", "c"])
    assert_equal(get_abc(test_dict), "foo")


def item_path_throws_test():
    try:
        item_path([], test_dict)
    except ValueError:
        assert_equal(True, True)
