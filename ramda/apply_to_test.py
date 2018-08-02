from .apply_to import apply_to
from .identity import identity
from .add import add
from ramda.private.asserts import assert_equal


def apply_nocurry_test():
    assert_equal(apply_to(42, identity), 42)
    assert_equal(apply_to(42, add(1)), 43)


def apply_curry_test():
    assert_equal(apply_to(42)(identity), 42)
    assert_equal(apply_to(42)(add(1)), 43)
