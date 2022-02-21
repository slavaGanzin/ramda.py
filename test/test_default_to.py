from ramda.default_to import default_to
from ramda.private.asserts import *

defaultTo42 = default_to(42)


def test_default_to():
    assert_equal(defaultTo42(None), 42)
    assert_equal(defaultTo42(""), "")
    assert_equal(defaultTo42("Ramda"), "Ramda")
    assert_equal(defaultTo42(0), 0)
