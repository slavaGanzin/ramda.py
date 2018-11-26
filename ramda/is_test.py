from ramda import *


def is_nocurry_test():
    assert is_(str, "foo")


def is_curry_test():
    assert is_(str)("foo")
