from ramda import join
from ramda.private.asserts import assert_equal


def test_reduce_nocurry():
    assert_equal(join(" ", ["aa", "bb", "cc"]), "aa bb cc")


def test_reduce_curry():
    assert_equal(join(" ")(["aa", "bb", "cc"]), "aa bb cc")
