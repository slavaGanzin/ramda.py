from ramda import *


def test_is_nocurry():
    assert is_(str, "foo")


def test_is_curry():
    assert is_(str)("foo")
