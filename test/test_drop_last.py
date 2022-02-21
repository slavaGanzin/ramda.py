from ramda.drop_last import drop_last
from ramda.private.asserts import *


def test_drop_nocurry():
    assert_iterables_equal(drop_last(2, [1, 2, 3, 4]), [1, 2])


def test_drop_curry():
    assert_iterables_equal(drop_last(2)([1, 2, 3, 4]), [1, 2])
