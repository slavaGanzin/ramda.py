from ramda import prop
from ramda.private.asserts import assert_equal


class TestObject:
    def __init__(self, val):
        self.val = val


test_object = TestObject("foo")


def test_prop_nocurry():
    assert_equal(prop("val", test_object), "foo")


def test_prop_curry():
    assert_equal(prop("val")(test_object), "foo")


def test_prop_nocurry_property():
    assert_equal(prop("val")({"val": "foo"}), "foo")
