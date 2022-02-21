from ramda import match
from ramda.private.asserts import assert_equal


def test_match_nocurry():
    assert_equal(match("a", "aa"), ["a", "a"])


def test_match_curry():
    assert_equal(match("a")("aa"), ["a", "a"])


def test_match_curry_regex():
    assert_equal(match(r"a+")("aa"), ["aa"])
