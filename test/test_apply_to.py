from ramda import apply_to
from ramda import identity
from ramda import add
from ramda.private.asserts import assert_equal


def test_apply_nocurry():
    assert_equal(apply_to(42, identity), 42)
    assert_equal(apply_to(42, add(1)), 43)


def test_apply_curry():
    assert_equal(apply_to(42)(identity), 42)
    assert_equal(apply_to(42)(add(1)), 43)
