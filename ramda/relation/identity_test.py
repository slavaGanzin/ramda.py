from .identity import identity
from ramda.private.asserts import assert_iterables_equal


def uniq_nocurry_test():
    assert_iterables_equal(identity(1), 1)
