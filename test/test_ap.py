from ramda import ap
from ramda import multiply
from ramda import add
from ramda import concat
from ramda import to_upper
from ramda.private.asserts import *


def test_ap_nocurry():
    assert_iterables_equal(
        ap([concat("tasty "), to_upper], ["pizza", "salad"]),
        ["tasty pizza", "tasty salad", "PIZZA", "SALAD"],
    )

    assert_iterables_equal(ap([multiply(2), add(3)], [1, 2, 3]), [2, 4, 6, 4, 5, 6])


def test_ap_curry():
    assert_iterables_equal(
        ap([concat("tasty "), to_upper])(["pizza", "salad"]),
        ["tasty pizza", "tasty salad", "PIZZA", "SALAD"],
    )

    assert_iterables_equal(ap([multiply(2), add(3)])([1, 2, 3]), [2, 4, 6, 4, 5, 6])


def test_ap_S_combinator():
    pass
    # assert_equal(ap(concat, toUpper)('Ramda'), 'RamdaRAMDA')
