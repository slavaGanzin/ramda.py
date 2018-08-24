from ramda.memoize import memoize
from ramda.product import product
from ramda.private.asserts import assert_equal as e


count = 0


def memoize_test():
    @memoize
    def factorial(n):
        global count
        count += 1
        return product(range(1, n + 1))

    e(factorial(5), 120)
    e(factorial(5), 120)
    e(factorial(5), 120)
    e(count, 1)
