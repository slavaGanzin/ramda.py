from ramda import *
from ramda.private.asserts import *


def string_append(s1, s2):
    return s1 + s2


def test_reduce_nocurry():
    assert_equal(reduce(string_append, "", ["aa", "bb", "cc"]), "aabbcc")


def test_reduce_curry():
    assert_equal(reduce(string_append, "")(["aa", "bb", "cc"]), "aabbcc")
