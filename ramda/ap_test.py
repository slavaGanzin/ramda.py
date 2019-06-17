from .ap import ap
from .multiply import multiply
from .add import add
from .concat import concat
from .to_upper import to_upper
from ramda.private.asserts import *


def ap_nocurry_test():
    assert_iterables_equal(
        ap([concat("tasty "), to_upper], ["pizza", "salad"]),
        ["tasty pizza", "tasty salad", "PIZZA", "SALAD"],
    )

    assert_iterables_equal(ap([multiply(2), add(3)], [1, 2, 3]), [2, 4, 6, 4, 5, 6])


def ap_curry_test():
    assert_iterables_equal(
        ap([concat("tasty "), to_upper])(["pizza", "salad"]),
        ["tasty pizza", "tasty salad", "PIZZA", "SALAD"],
    )

    assert_iterables_equal(ap([multiply(2), add(3)])([1, 2, 3]), [2, 4, 6, 4, 5, 6])


def ap_S_combinator_test():
    pass
    # assert_equal(ap(concat, toUpper)('Ramda'), 'RamdaRAMDA')
