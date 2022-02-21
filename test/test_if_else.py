from ramda import if_else
from ramda.inc import inc
from ramda.dec import dec
from ramda.private.asserts import assert_equal


def positive(x):
    return x > 0


def test_if_else_nocurry():
    assert_equal(if_else(positive, inc, dec, 5), 6)
    assert_equal(if_else(positive, inc, dec, -5), -6)


def test_if_else_curry():
    inc_away_from_zero = if_else(positive, inc, dec)
    assert_equal(inc_away_from_zero(5), 6)
    assert_equal(inc_away_from_zero(-5), -6)
