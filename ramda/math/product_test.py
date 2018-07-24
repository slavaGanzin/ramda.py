from .product import product
from ramda.private.asserts import assert_equal


def product_test():
    assert_equal(product([2, 3, 5]), 30)
