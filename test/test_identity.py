from ramda import identity
from ramda.private.asserts import assert_equal


def test_identity():
    assert_equal(identity(3), 3)
