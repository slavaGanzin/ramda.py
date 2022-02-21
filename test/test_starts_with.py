from ramda import *
from ramda.private.asserts import *


def test_starts_with():
    assert_equal(starts_with("a", "abc"), True)
    assert_equal(starts_with("b", "abc"), False)
    assert_equal(starts_with(["a"], ["a", "b", "c"]), True)
    assert_equal(starts_with(["b"], ["a", "b", "c"]), False)
