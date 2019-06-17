from .match import match
from ramda.private.asserts import assert_equal


def match_nocurry_test():
    assert_equal(match("a", "aa"), ["a", "a"])


def match_curry_test():
    assert_equal(match("a")("aa"), ["a", "a"])


def match_curry_regex_test():
    assert_equal(match(r"a+")("aa"), ["aa"])
