from ramda import replace
from ramda.private.asserts import assert_equal


def test_replace_nocurry():
    assert_equal(replace("a", "b", "aa"), "bb")


def test_replace_curry():
    assert_equal(replace("a", "b")("aa"), "bb")


def test_replace_curry_regex():
    assert_equal(replace(r"a+", "b")("aa"), "b")
