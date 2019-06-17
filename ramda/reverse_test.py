from ramda import *
from ramda.private.asserts import *


def reverse_test():
    assert_equal(reverse([1, 2, 3]), [3, 2, 1])
    assert_equal(reverse([1, 2]), [2, 1])
    assert_equal(reverse([1]), [1])
    assert_equal(reverse([]), [])

    assert_equal(reverse("abc"), "cba")
    assert_equal(reverse("ab"), "ba")
    assert_equal(reverse("a"), "a")
    assert_equal(reverse(""), "")
