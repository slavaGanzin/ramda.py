from ramda import product
from ramda.private.asserts import assert_equal


def test_product():
    assert_equal(product([2, 3, 5]), 30)
