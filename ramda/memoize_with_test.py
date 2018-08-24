from ramda.memoize_with import memoize_with
from ramda.product import product
from ramda.private.asserts import assert_equal as e


count = 0


def memoize_with_test():
    @memoize_with(lambda x: -x)
    def factorial(n):
        global count
        count += 1
        return product(range(1, n + 1))

    e(factorial(5), 120)
    e(factorial(5), 120)
    e(factorial(5), 120)
    e(factorial(4), 24)
    e(factorial(4), 24)
    e(factorial(4), 24)
    e(factorial(4), 24)
    e(count, 2)
