from ramda.private.asserts import *
from ramda.eq_by import eq_by


def test_eq_by():
    assert_equal(eq_by(abs, 5, -5), True)
    assert_equal(eq_by(abs, 5, -6), False)
